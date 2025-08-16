from supabase_init import supabase

class DishModel:
    table_name = "dishes"

    @staticmethod
    def create_dish(photo, dishname, quantity, price):
        data = {
            "photo": photo,
            "dishname": dishname,
            "quantity": quantity,
            "price": price
        }
        response = supabase.table(DishModel.table_name).insert(data).execute()
        return response.data

    @staticmethod
    def get_all_dishes():
        response = supabase.table(DishModel.table_name).select("*").execute()
        return response.data

    @staticmethod
    def get_dish_by_id(dish_id):
        response = supabase.table(DishModel.table_name).select("*").eq("id", dish_id).execute()
        return response.data[0] if response.data else None

    @staticmethod
    def update_dish(dish_id, updates):
        response = supabase.table(DishModel.table_name).update(updates).eq("id", dish_id).execute()
        return response.data

    @staticmethod
    def delete_dish(dish_id):
        response = supabase.table(DishModel.table_name).delete().eq("id", dish_id).execute()
        return response.data
