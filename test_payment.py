#!/usr/bin/env python3
"""
Unit and integration tests for the Lotus Hut Payment APIs
Tests order creation, price calculations, coupons, server-side payment verification,
and simulation scenarios (success, failure, cancel).
"""

import unittest
import json
from app import app, ORDERS_STORE

class PaymentApiTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_01_config_endpoint(self):
        resp = self.app.get('/api/config')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        self.assertEqual(data['payment_mode'], 'test')
        self.assertTrue(data['is_test_mode'])

    def test_02_coupons_endpoint(self):
        resp = self.app.get('/api/coupons')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        codes = [c['code'] for c in data['coupons']]
        self.assertIn('SWIGGY50', codes)

    def test_03_create_order(self):
        payload = {
            "items": [
                {"id": "cf_1", "name": "Lotus Special Cold Coffee", "price": 150, "count": 2},
                {"id": "bg_1", "name": "Cheesy Burger", "price": 120, "count": 1}
            ],
            "customer": {
                "name": "Amit Verma",
                "phone": "9876543210",
                "vehicle": "MP 09 AB 1234",
                "spot": "Bay 3",
                "notes": "Extra tissues"
            },
            "coupon_code": "SWIGGY50"
        }
        resp = self.app.post('/api/create-order', data=json.dumps(payload), content_type='application/json')
        self.assertEqual(resp.status_code, 200)
        data = resp.get_json()
        self.assertTrue(data['success'])
        self.assertTrue(data['order_id'].startswith('LH-'))
        self.assertEqual(data['bill']['item_total'], 420.0) # 150*2 + 120 = 420
        self.assertEqual(data['bill']['delivery_fee'], 0.0) # >= 199 is free
        self.assertEqual(data['bill']['taxes'], 21.0) # 5% of 420 = 21
        self.assertEqual(data['bill']['discount'], 50.0) # SWIGGY50 applied
        self.assertEqual(data['bill']['payable_amount'], 391.0) # 420 + 0 + 21 - 50 = 391
        self.assertIn('verification_token', data)

    def test_04_simulate_success_and_verify(self):
        # 1. Create order
        create_resp = self.app.post('/api/create-order', data=json.dumps({
            "items": [{"id": "cf_1", "name": "Cold Coffee", "price": 150, "count": 1}],
            "customer": {"name": "Sim Tester", "vehicle": "MP 09 CD 5678", "phone": "9876543210"}
        }), content_type='application/json')
        order_data = create_resp.get_json()
        order_id = order_data['order_id']

        # 2. Simulate payment success
        sim_resp = self.app.post('/api/simulate-payment', data=json.dumps({
            "order_id": order_id,
            "scenario": "success",
            "payment_method": "UPI",
            "method_details": {"app": "Google Pay", "upi_id": "test@okhdfcbank"}
        }), content_type='application/json')
        self.assertEqual(sim_resp.status_code, 200)
        sim_data = sim_resp.get_json()
        self.assertEqual(sim_data['scenario'], 'success')
        self.assertTrue(sim_data['payment_id'].startswith('pay_test_'))

        # 3. Verify on server
        verify_resp = self.app.post('/api/verify-payment', data=json.dumps({
            "order_id": order_id,
            "payment_id": sim_data['payment_id'],
            "verification_token": sim_data['verification_token'],
            "payment_method": "UPI",
            "method_details": {"app": "Google Pay", "upi_id": "test@okhdfcbank"}
        }), content_type='application/json')
        self.assertEqual(verify_resp.status_code, 200)
        v_data = verify_resp.get_json()
        self.assertTrue(v_data['success'])
        self.assertEqual(v_data['status'], 'PAID')
        self.assertTrue(v_data['transaction_id'].startswith('TXN_TEST_'))

    def test_05_simulate_failure(self):
        # 1. Create order
        create_resp = self.app.post('/api/create-order', data=json.dumps({
            "items": [{"id": "cf_1", "name": "Cold Coffee", "price": 150, "count": 1}],
            "customer": {"name": "Sim Tester", "vehicle": "MP 09 CD 5678", "phone": "9876543210"}
        }), content_type='application/json')
        order_id = create_resp.get_json()['order_id']

        # 2. Simulate payment failure
        sim_resp = self.app.post('/api/simulate-payment', data=json.dumps({
            "order_id": order_id,
            "scenario": "failure",
            "payment_method": "CARD"
        }), content_type='application/json')
        self.assertEqual(sim_resp.status_code, 402)
        sim_data = sim_resp.get_json()
        self.assertFalse(sim_data['success'])
        self.assertEqual(sim_data['status'], 'FAILED')
        self.assertTrue(sim_data['can_retry'])
        self.assertIn('error_message', sim_data)

    def test_06_simulate_cancel(self):
        # 1. Create order
        create_resp = self.app.post('/api/create-order', data=json.dumps({
            "items": [{"id": "cf_1", "name": "Cold Coffee", "price": 150, "count": 1}],
            "customer": {"name": "Sim Tester", "vehicle": "MP 09 CD 5678", "phone": "9876543210"}
        }), content_type='application/json')
        order_id = create_resp.get_json()['order_id']

        # 2. Simulate payment cancel
        sim_resp = self.app.post('/api/simulate-payment', data=json.dumps({
            "order_id": order_id,
            "scenario": "cancelled",
            "payment_method": "NETBANKING"
        }), content_type='application/json')
        self.assertEqual(sim_resp.status_code, 200)
        sim_data = sim_resp.get_json()
        self.assertFalse(sim_data['success'])
        self.assertEqual(sim_data['status'], 'CANCELLED')
        self.assertTrue(sim_data['can_retry'])

if __name__ == '__main__':
    unittest.main()
