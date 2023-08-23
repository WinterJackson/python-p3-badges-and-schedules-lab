def badge_maker(name):
    return "Hello, my name is " + name + "."

def batch_badge_creator(names):
    badge_messages = []
    for name in names:
        badge_messages.append(badge_maker(name))
    return badge_messages

speaker_names = ["Arel", "Carol"]
speaker_name = "John"
print (badge_maker(speaker_name))
badge_messages = batch_badge_creator(speaker_names)
print(badge_messages)

def assign_rooms(speakers):
    room_assignments = []
    for index, speaker in enumerate(speakers, start=1):
        room_assignment = f"Hello, {speaker}! You'll be assigned to room {index}!"
        room_assignments.append(room_assignment)
    return room_assignments

speaker_names = ["Arel", "Carol"]
room_assignments = assign_rooms(speaker_names)
print(room_assignments)

def printer(speaker_names):
    badge_messages = batch_badge_creator(speaker_names)
    room_assignments = assign_rooms(speaker_names)
    
    for badge_message in badge_messages:
        print(badge_message)
    
    for room_assignment in room_assignments:
        print(room_assignment)

speaker_names = ["Arel", "Carol"]
printer(speaker_names)
