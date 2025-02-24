class Member:
    def __init__(self, memberID, name, membershipType):
        self.memberID = memberID
        self.name = name
        self.membershipType = membershipType

    def getMemberInfo(self):
        return f"{self.memberID} {self.name} {self.membershipType}"

class MembershipPlan:
    def __init__(self, planID, planName, fee):
        self.planID = planID
        self.planName = planName
        self.fee = fee

    def getPlanDetails(self):
        return f"{self.planName} {self.planID}"

class Gym:
    def __init__(self, members, plans):
        self.members = members
        self.plans = plans

    def registerMember(self, member):
        self.members.append(member)

    def assignPlan(self, memberID, planID):
        member_found = False
        plan_found = False

        for m in self.members:
            if m.memberID == memberID:
                member_found = True
                member = m
                break

        for p in self.plans:
            if p.planID == planID:
                plan_found = True
                plan = p
                break

        if member_found and plan_found:
            member.membershipType = plan.planName  
            return True
        return False

def main():
    # Create members and membership plans
    member1 = Member(1, "David", "monthly")
    member2 = Member(2, "Linda", "yearly")
    plan1 = MembershipPlan(101, "Standard", 50.0)
    plan2 = MembershipPlan(102, "Premium", 80.0)

    # Create gym instance and register members and plans
    gym = Gym([member1, member2], [plan1, plan2])  # Pass plans and members during initialization

    # Test assigning membership plans
    assign1 = gym.assignPlan(member1.memberID, plan1.planID)
    assign2 = gym.assignPlan(member2.memberID, plan2.planID)

    # Output results
    print("Plan assigned to David:", assign1)
    print("Plan assigned to Linda:", assign2)

    # Attempt assignment for a non-existent member
    assign_invalid = gym.assignPlan(999, plan1.planID)
    print("Plan assignment to non-existent member:", assign_invalid)

if __name__ == '__main__':
    main()
