import random
from util import Queue


class User:
    def __init__(self, name):
        self.name = name


class SocialGraph:
    def __init__(self):
        # id of the last added user
        self.last_id = 0
        self.users = {}
        self.friendships = {}

    # add edge
    def add_friendship(self, user_id, friend_id):
        """
        Creates a bi-directional friendship
        """
        if user_id == friend_id:
            print("WARNING: You cannot be friends with yourself")
        elif (
            friend_id in self.friendships[user_id]
            or user_id in self.friendships[friend_id]
        ):
            print("WARNING: Friendship already exists")
        else:
            self.friendships[user_id].add(friend_id)
            self.friendships[friend_id].add(user_id)

    # add vertex
    def add_user(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.last_id += 1  # automatically increment the ID to assign the new user
        self.users[self.last_id] = User(name)
        self.friendships[self.last_id] = set()

    def populate_graph(self, num_users, avg_friendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.last_id = 0
        self.users = {}
        self.friendships = {}

        # Add users using the add_user num_user times

        # Create random friendships
        for i in range(0, num_users):
            self.add_user(f"User {i + 1}")
        # generate all friendship combinations
        possible_friendships = []
        # avoid duplicates by making sure first number is smaller than second
        for user_id in self.users:
            for friend_id in range(user_id + 1, self.last_id + 1):
                possible_friendships.append((user_id, friend_id))
        # shuffle all possible friendships
        random.shuffle(possible_friendships)
        # create for first x pairs, where x is half the number of friends, because each connection creates two friendships
        for i in range((num_users * avg_friendships) // 2):
            friendship = possible_friendships[i]
            self.add_friendship(friendship[0], friendship[1])

    def get_friends(self, user_id):
        if user_id in self.users:
            return self.friendships[user_id]
        else:
            return None

    def get_all_social_paths(self, user_id):
        """
        Takes a user's user_id as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.

        What are the keywords in the above problem?
        - "shortest path" tells us breadth first. Depth first does not guarantee the shortest path
        - "extended network" tells us we need to use a traversal, and that it is connected component

        planning:
        - graph was already built
        - start at given user_id, do a BFT, and return the path to each friend

        pseudocode traversal:
        - create queue
        - enqueue path
        - create visited dictionary
        - while queue is not empty:
            - dequeue first path
            - if not visited
                - do the thing!
                - add to visited
                - for each neighbor 
                    - copy path and enqueue  
        """
        queue = Queue()
        queue.enqueue([user_id])  # we enqueue a list to build our path
        visited = {}
        while queue.size() > 0:
            path = queue.dequeue()
            if path[-1] not in visited.keys():
                visited[path[-1]] = path
                for next_friend in self.get_friends(path[-1]):
                    new_path = list(path)
                    new_path.append(next_friend)
                    queue.enqueue(new_path)
        return visited


if __name__ == "__main__":
    sg = SocialGraph()
    sg.populate_graph(10, 2)
    print("sg.friendships", sg.friendships)
    connections = sg.get_all_social_paths(1)
    print("connections", connections)
