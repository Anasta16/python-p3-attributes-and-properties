#!/usr/bin/env python3

# class Dog:

#     def get_name(self):
#         return self._name
#     def set_name(self, name):
#         if (type(name) == str) and (0 < len(name) <= 25):
#             self._name = name
#         else:
#             print("Name must be string between 1 and 25 characters.")

#     name = property(get_name, set_name)

#     def get_breed(self):
#         return self._breed
#     def set_breed(self, breed):
#         approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]
#         for x in approved_breeds:
#             if x == breed:
#                 self._breed = breed
#                 break
#             else:
#                 self._breed = None
#         if self._breed == None:
#             print("Breed must be in list of approved breeds.")
#     breed = property(get_breed, set_breed)

class Dog:

    def get_name(self):
        return self._name

    def set_name(self, name):
        if (type(name) == str) and (0 < len(name) < 25):
            self._name = name
        else:
            print("Name must be string between 1 and 25 characters.")

    name = property(get_name, set_name)

    def get_breed(self):
        return self._breed
    def set_breed(self, breed):
        approved_breeds = ["Mastiff", "Chihuahua", "Corgi", "Shar Pei", "Beagle", "French Bulldog", "Pug", "Pointer"]

        for x in approved_breeds:
            if x == breed:
                self._breed = breed
                break
            else:
                self._breed = None
        if self._breed == None:
            print("Breed must be in list of approved breeds.")
    breed = property(get_breed, set_breed)