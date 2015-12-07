from rest_framework import permissions


class IsOwnerOrInGroupOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit it.
    Other authenticated users can read but not edit.
    """

    def has_object_permission(self, request, view, obj):
        print(request.user, "is tryna")

        print("Checking permissions for", str(request), str(obj))

        if request.user.is_authenticated():

            # Write permissions are only allowed to the author of the report.
            if obj.author == request.user:
                print("Author is user -> access granted.")
                return True

            # Read permissions are allowed to either:
            #   all authenticated users if obj.group == None
            #   all members of group if obj.group != None

            # GET, HEAD or OPTIONS requests
            if request.method in permissions.SAFE_METHODS:
                print("User is reading, not writing...")
                if obj.group_name:
                    print("Object is in a group.")
                    if obj.group_name.lower() == 'public':
                        print("Object's group is public -> access granted.")
                        return True
                    if obj.group_name == request.user.group_name:
                        print("Object's group == request's group -> access granted.")
                    else:
                        print("Object's group != request's group -> access denied.")
                    return obj.group_name == request.user.group_name
                else:
                    # object has no group, so all authenticated can access
                    print("Object has no group -> access granted.")
                    return True

            return False

        else:
            print("User is not authenticated -> access denied.")
            return False

