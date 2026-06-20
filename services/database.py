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


def release_exists(release_id):
    response = (
        supabase
        .table("known_releases")
        .select("*")
        .eq("release_id", release_id)
        .execute()
    )

    return len(response.data) > 0


def save_release(artist, release_id):

    if release_exists(release_id):
        return

    supabase.table("known_releases").insert({
        "artist": artist,
        "release_id": release_id
    }).execute()


def get_tracked_artists():
    response = (
        supabase
        .table("tracked_artists")
        .select("artist")
        .execute()
    )

    return [row["artist"] for row in response.data]


def add_tracked_artist(artist):
    existing = (
        supabase
        .table("tracked_artists")
        .select("*")
        .eq("artist", artist)
        .execute()
    )

    if existing.data:
        return False

    supabase.table("tracked_artists").insert({
        "artist": artist
    }).execute()

    return True
def get_subscribers(artist):
    response = (
        supabase
        .table("subscriptions")
        .select("user_id")
        .eq("artist", artist)
        .execute()
    )

    return [row["user_id"] for row in response.data]