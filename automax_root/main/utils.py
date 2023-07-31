def user_listing_path(instance, filename):
    return "user_{0}/listings/{1}".format(instance.seller.user.id, filename)


# I think "instance" refer to current model in the specific app.