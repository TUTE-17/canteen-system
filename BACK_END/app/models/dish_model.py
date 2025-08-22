from supabase_init import supabase

class DishModel:
    table_name = "dishes"


    @staticmethod
    def get_all_dishes():
        response = supabase.table(DishModel.table_name).select("*").execute()
        return response.data

    
    @staticmethod
    def get_dish_by_id(dish_id):
        response = supabase.table(DishModel.table_name).select("*").eq("id", dish_id).single().execute()
        return response.data  

    @staticmethod
    def create_dish(photo, dishname, quantity, price, available=True):
        data = {
            "photo": photo,
            "dishname": dishname,
            "quantity": quantity,
            "price": price,
            "available": available
        }
        response = supabase.table(DishModel.table_name).insert(data).execute()
        if response.data:
            return response.data[0]
        return {"error": "Failed to insert dish"}

    @staticmethod
    def update_dish(dish_id, updates):
        response = supabase.table(DishModel.table_name).update(updates).eq("id", dish_id).execute()
        if response.data:
            return response.data[0] 
        return {"error": "Failed to update dish"}
    
    @staticmethod
    def delete_dish(dish_id):
        try:
            
            response = supabase.table(DishModel.table_name).delete().eq("id", dish_id).execute()
           
            if response.data and len(response.data) > 0:
                return True
            return False
        except Exception as e:
            print("Error deleting dish:", e)
            return False
   