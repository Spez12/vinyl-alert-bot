from services.supabase_client import supabase


def add_subscription(user_id, artist):
    existing = (
        supabase
        .table("subscriptions")
        .select("*")
        .eq("user_id", user_id)
        .eq("artist", artist)
        .execute()
    )

    if existing.data:
        return False

    supabase.table("subscriptions").insert({
        "user_id": user_id,
        "artist": artist
    }).execute()

    return True


def remove_subscription(user_id, artist):
    supabase.table("subscriptions") \
        .delete() \
        .eq("user_id", user_id) \
        .eq("artist", artist) \
        .execute()


def get_subscriptions(user_id):
    response = (
        supabase
        .table("subscriptions")
        .select("artist")
        .eq("user_id", user_id)
        .execute()
    )

    return [row["artist"] for row in response.data]