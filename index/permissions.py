from rest_framework import permissions


class IsOwnerOrInGroupOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Other authenticated users can read but not edit.
    """

    def has_object_permission(self, request, view, obj):
        print('\n', request.user, "is tryna")

        print("\tChecking permissions for:", obj.title)
        print('\t', dir(request.user))
        print('\t', dir(obj))

        if request.user.is_authenticated():

            # Write permissions are only allowed to the author of the report.
            if obj.author == request.user:
                print("\t\tAuthor is user -> r/w access granted.")
                return True

            # Read permissions are allowed to either:
            #   all authenticated users if obj.group == None
            #   all members of group if obj.group != None

            # GET, HEAD or OPTIONS requests
            if request.method in permissions.SAFE_METHODS:
                print("\t\tUser is reading, not writing...")
                if obj.group_name:
                    print("\t\t\tObject is in a group.")
                    if obj.group_name.lower() == 'public':
                        print("\t\t\t\tObject's group is public -> read access granted.")
                        return True
                    if obj.group_name in request.user.groups:
                        print("\t\t\t\tObject's group == request's group -> read access granted.")
                    else:
                        print("\t\t\t\tObject's group != request's group -> read access denied.")
                    return obj.group_name == request.user.groups
                else:
                    # object has no group, so all authenticated can access
                    print("\t\t\tObject has no group -> read access granted.")
                    return True

            print("\t\tNot allowed for", obj.title)
            return False

        else:
            print("\tUser is not authenticated -> r/w access denied.")
            return False

