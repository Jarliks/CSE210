class Collection:
    """A collection of things.

    Attributes:
        _things (dict): A dictionary of things { key: group_name, value: a list of things }
    """

    def __init__(self):
        """Constructs a new Collection."""
        self._things = {}
        
    def add_thing(self, group, thing):
        """Adds an thing to the given group.
        
        Args:
            group (string): The name of the group.
            thing (thing): The thing to add.
        """
        if not group in self._things.keys():
            self._things[group] = []
            
        if not thing in self._things[group]:
            self._things[group].append(thing)

    def get_things(self, group):
        """Gets the things in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The things in the group.
        """
        results = []
        if group in self._things.keys():
            results = self._things[group].copy()
        return results
    
    def get_all_things(self):
        """Gets all of the things in the cast.
        
        Returns:
            List: All of the things in the cast.
        """
        results = []
        for group in self._things:
            results.extend(self._things[group])
        return results

    def get_first_thing(self, group):
        """Gets the first thing in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first thing in the group.
        """
        result = None
        if group in self._things.keys():
            result = self._things[group][0]
        return result

    def remove_thing(self, group, thing):
        """Removes an thing from the given group.
        
        Args:
            group (string): The name of the group.
            thing (thing): The thing to remove.
        """
        if group in self._things:
            self._things[group].remove(thing)