I was correct.

The count field being printed is a member of the Player class and not of the instance. The count being updated in the initializer is an instance field.

What I learned from the explanation:
`self.count` will look up the class level value for the value to increment. However when it sets that value it will set it into the instance field and will then shadow the class level for this instance.
