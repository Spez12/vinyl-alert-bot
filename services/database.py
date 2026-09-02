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
    (
        supabase
        .table("subscriptions")
        .delete()
        .eq("user_id", user_id)
        .eq("artist", artist)
        .execute()
    )


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


def get_tracked_artist(artist):
    """Restituisce il nome canonico salvato in tracked_artists.

    Il confronto è case-insensitive, così /sub artista funziona
    anche se l'utente non usa la stessa capitalizzazione del database.
    """
    target = artist.strip().casefold()

    for tracked_artist in get_tracked_artists():
        if tracked_artist.strip().casefold() == target:
            return tracked_artist

    return None


def add_tracked_artist(artist):
    artist = artist.strip()

    if not artist:
        return False

    if get_tracked_artist(artist) is not None:
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


def remove_tracked_artist(artist):
    tracked_artist = get_tracked_artist(artist)

    if tracked_artist is None:
        return False

    (
        supabase
        .table("tracked_artists")
        .delete()
        .eq("artist", tracked_artist)
        .execute()
    )

    return True
