def create_profile(**details):
    return details
profile = create_profile(
    name="Michael",
    age=22,
    country="Nigeria",
    bio="I am a software engineer",
    sex="Male",
    height=178.7,
    religion="Christian",
    marital_status="Single"
)

print(profile)