from supabase_init import supabase

class PaymentModel:
    table_name = "orders"

    @staticmethod
    def update_payment_status(order_id, status, razorpay_payment_id=None):
        """
        Update the payment status and optionally store Razorpay payment ID.
        """
        data = {"status": status}
        if razorpay_payment_id:
            data["razorpay_id"] = razorpay_payment_id

        response = supabase.table(PaymentModel.table_name).update(data).eq("id", order_id).execute()
        return response
