class RoleBuilder:
    """
    Private data member
    """
    ROLES = ["UNDEFINED", "DEVELOPER", "TEST_ENGINEER", "SR_DEVELOPER", "DESIGNER"]

    """
    Method to get role description for a given role id
    """
    @staticmethod
    def get_role_description(role_id):
        # Support enum or integer role identifiers
        try:
            rid = role_id.value if hasattr(role_id, "value") else int(role_id)
        except (TypeError, ValueError):
            return RoleBuilder.ROLES[0]

        if 1 <= rid <= 4:
            return RoleBuilder.ROLES[rid]
        return RoleBuilder.ROLES[0]
