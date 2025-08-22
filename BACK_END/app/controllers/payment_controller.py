import razorpay
from models.payment_model import PaymentModel
from config import RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY


razorpay_client = razorpay.Client(auth=(RAZORPAY_KEY_ID, RAZORPAY_SECRET_KEY))

class PaymentController:

    @staticmethod
    def create_order(order_id, amount):
        """
        Create Razorpay order and return details.
        Amount must be in paise (integer).
        """
        try:
            amount = int(float(amount) * 100) 
            data = {
                "amount": amount,
                "currency": "INR",
                "receipt": f"order_rcptid_{order_id}",
                "payment_capture": 1
            }
            order = razorpay_client.order.create(data=data)

            return {
                "status": "success",
                "order_id": order["id"],
                "amount": order["amount"],
                "currency": order["currency"],
                "key_id": RAZORPAY_KEY_ID
            }

        except Exception as e:
            return {"status": "failed", "message": f"Order creation failed: {str(e)}"}

    @staticmethod
    def verify_payment(order_id, razorpay_payment_id, razorpay_order_id, razorpay_signature):
        """
        Verify Razorpay signature and update Supabase.
        """
        try:
            params_dict = {
                "razorpay_order_id": razorpay_order_id,
                "razorpay_payment_id": razorpay_payment_id,
                "razorpay_signature": razorpay_signature
            }

            
            razorpay_client.utility.verify_payment_signature(params_dict)

        
            PaymentModel.update_payment_status(order_id, "paid", razorpay_payment_id)

            return {"status": "success", "message": "Payment verified successfully! ✅"}

        except Exception as e:
            PaymentModel.update_payment_status(order_id, "failed")
            return {"status": "failed", "message": f"Payment verification failed ❌ {str(e)}"}
