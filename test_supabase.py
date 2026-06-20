from services.supabase_client import supabase

response = (
    supabase
    .table("subscriptions")
    .select("*")
    .execute()
)

print(response.data)