from supabase_init import supabase

class OrderModel:
    @staticmethod
    def create_order(student_regno, total):
        order_data = {
            "student_regno": student_regno,
            "status": "pending",
            "price": total
        }
        result = supabase.table("orders").insert(order_data).execute()
        return result.data[0] if result.data else None

    @staticmethod
    def add_order_item(order_id, dish, quantity, price):
        item_data = {
            "order_id": order_id,
            "dishname": dish,
            "quantity": quantity,
            "price": price
        }
        return supabase.table("order_items").insert(item_data).execute()

    @staticmethod
    def get_orders():
        orders_res = supabase.table("orders").select("*").execute()
        orders = orders_res.data if orders_res.data else []

        for order in orders:
            items_res = supabase.table("order_items").select("*").eq("order_id", order["id"]).execute()
            order["items"] = items_res.data if items_res.data else []


            student_res = supabase.table("students").select("regno").eq("regno", order.get("student_regno")).execute()
            order["student"] = {"reg_no": student_res.data[0]["regno"]} if student_res.data else {"reg_no": "N/A"}

        return orders

    @staticmethod
    def delete_order(order_id):
        supabase.table("order_items").delete().eq("order_id", order_id).execute()
        return supabase.table("orders").delete().eq("id", order_id).execute()
