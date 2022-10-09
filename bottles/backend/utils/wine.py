import os


class WineUtils:

    @staticmethod
    def get_user_dir(prefix_path: str):
        ignored = ["Public"]
        usersdir = os.path.join(prefix_path, "drive_c", "users")
        if found := [
            user_dir
            for user_dir in os.listdir(usersdir)
            if user_dir not in ignored
        ]:
            return found[0]
        else:
            raise Exception("No user directories found.")
