from models.order_model import OrderModel

class OrderController:
    @staticmethod
    def create_new_order(data):
        student_regno = data.get("student_regno")
        items = data.get("items", [])
        total = sum(item["quantity"] * item["price"] for item in items)

        
        from supabase_init import supabase
        student_check = supabase.table("students").select("*").eq("regno", student_regno).execute()
        if not student_check.data:
            return {"success": False, "message": "Invalid student regno"}

        order = OrderModel.create_order(student_regno, total)
        if not order:
            return {"success": False, "message": "Order creation failed"}

        order_id = order["id"]
        for item in items:
            OrderModel.add_order_item(order_id, item["dishname"], item["quantity"], item["price"])

        return {"success": True, "order_id": order_id}

    @staticmethod
    def get_orders():
        return OrderModel.get_orders()

    @staticmethod
    def delete_order(order_id):
        result = OrderModel.delete_order(order_id)
        if not result.data:
         return {"success": False, "message": "Order not found"}

        return {"success": True, "message": "Order deleted successfully"}
