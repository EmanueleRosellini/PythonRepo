import os
import argparse

class DirectoryWalk:
    def __init__(self):
        self.path = ""

    @staticmethod
    def get_args():
        parser = argparse.ArgumentParser(description="Scan all files")
        parser.add_argument("path", help="Path where to scan")
        return parser.parse_args()


    def scan(self):
        with os.scandir(self.path) as entries:
            for entry in entries:
                if entry.is_file():
                    print(entry.name)


    def main(self):
        args = self.get_args()
        self.path = args.path
        self.scan()

if __name__ == "__main__":
    walk_instance = DirectoryWalk()
    walk_instance.main()

