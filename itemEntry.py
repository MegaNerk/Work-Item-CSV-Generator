from enum import Enum
import date_handler

class Prio(Enum):
    LOW = 0
    MEDIUM = 1
    HIGH = 2

class Status(Enum):
    NOT_STARTED = 0
    IN_PROGRESS = 1
    COMPLETE = 2
    ON_HOLD = 3
    CANCELLED = 4
    DELAYED = 5
    PLANNED = 6
    SCHEDULED = 7
    IN_REVIEW = 8
    APPROVED = 9
    REJECTED = 10
    BLOCKED = 11
    AWAITING_APPROVAL = 12
    AWAITING_INPUT = 13
    READY_FOR_DEPLOYMENT = 14
    DEPLOYED = 15
    ROLLED_BACK = 16
    UNDER_TEST = 17
    TESTING_FAILED = 18
    TESTING_PASSED = 19
    ARCHIVED = 20
    CLOSED = 21
    REOPENED = 22
    IN_QA = 23
    QA_PASSED = 24
    QA_FAILED = 25
    MIGRATING = 26
    MIGRATION_COMPLETE = 27
    DESIGN_PHASE = 28
    DEVELOPMENT_PHASE = 29
    STAGING = 30
    UAT = 31
    FINALIZED = 32

class ItemType(Enum):
    FINANCIAL = 0
    SOFTWARE = 1
    MANAGERIAL = 2
    ACCOUNTING = 3
    BUDGETING = 4
    PAYROLL = 5
    TAXATION = 6
    INVOICING = 7
    AUDITING = 8
    INVESTMENT = 9
    PROCUREMENT = 10
    SALES = 11
    CRM = 12
    ERP = 13
    LOGISTICS = 14
    INVENTORY = 15
    ANALYTICS = 16
    DATA_SCIENCE = 17
    MACHINE_LEARNING = 18
    ARTIFICIAL_INTELLIGENCE = 19
    CYBERSECURITY = 20
    CLOUD_COMPUTING = 21
    DEVOPS = 22
    INFRASTRUCTURE = 23
    NETWORKING = 24
    IT_SUPPORT = 25
    SOFTWARE_ENGINEERING = 26
    QA_TESTING = 27
    DATABASE_MANAGEMENT = 28
    WEB_DEVELOPMENT = 29
    MOBILE_DEVELOPMENT = 30
    UI_UX = 31
    PRODUCT_MANAGEMENT = 32
    PROJECT_MANAGEMENT = 33
    STRATEGY = 34
    RISK_MANAGEMENT = 35
    OPERATIONS = 36
    COMPLIANCE = 37
    LEGAL = 38
    CONTRACTS = 39
    LITIGATION = 40
    PATENTS = 41
    HR = 42
    RECRUITMENT = 43
    ONBOARDING = 44
    EMPLOYEE_RELATIONS = 45
    PAYROLL_MANAGEMENT = 46
    BENEFITS = 47
    TRAINING = 48
    PERFORMANCE = 49
    RETENTION = 50
    OFFBOARDING = 51
    MARKETING = 52
    ADVERTISING = 53
    BRANDING = 54
    SEO = 55
    CONTENT_MARKETING = 56
    SOCIAL_MEDIA = 57
    EMAIL_MARKETING = 58
    EVENTS = 59
    CAMPAIGNS = 60
    PUBLIC_RELATIONS = 61
    CUSTOMER_SUPPORT = 62
    CLIENT_RELATIONS = 63
    USER_RESEARCH = 64
    COMMUNITY = 65
    TRAINING_DEV = 66
    DOCUMENTATION = 67
    PRODUCT_SUPPORT = 68
    SOFTWARE_SUPPORT = 69
    HARDWARE_SUPPORT = 70
    PROCUREMENT_IT = 71
    SECURITY_OPERATIONS = 72
    INCIDENT_RESPONSE = 73
    ACCESS_CONTROL = 74
    GOVERNANCE = 75
    INTERNAL_AUDIT = 76
    EXTERNAL_AUDIT = 77
    COMPLIANCE_IT = 78
    INCIDENT_MANAGEMENT = 79
    DISASTER_RECOVERY = 80
    BACKUP = 81
    DATA_GOVERNANCE = 82
    DATA_PRIVACY = 83
    GDPR = 84
    CCPA = 85
    REGULATORY = 86
    ACCOUNT_MANAGEMENT = 87
    LICENSE_MANAGEMENT = 88
    VENDOR_MANAGEMENT = 89
    SUPPLY_CHAIN = 90
    TRANSPORTATION = 91
    SHIPPING = 92
    WAREHOUSING = 93
    FULFILLMENT = 94
    ECOMMERCE = 95
    RETAIL = 96
    WHOLESALE = 97
    PROCUREMENT_GENERAL = 98
    QUALITY_CONTROL = 99
    INDUSTRIAL_ENGINEERING = 100
    MANUFACTURING = 101
    MECHANICAL_ENGINEERING = 102
    ELECTRICAL_ENGINEERING = 103
    CIVIL_ENGINEERING = 104
    ARCHITECTURE = 105
    ENVIRONMENTAL = 106
    CHEMICAL_ENGINEERING = 107
    BIOMEDICAL = 108
    RESEARCH = 109
    DEVELOPMENT = 110
    INNOVATION = 111
    LAB_TESTING = 112
    FIELD_TESTING = 113
    MAINTENANCE = 114
    REPAIRS = 115
    INSPECTIONS = 116
    SCHEDULING = 117
    PLANNING = 118
    COST_ESTIMATION = 119
    RESOURCE_MANAGEMENT = 120
    STAFFING = 121
    KNOWLEDGE_MANAGEMENT = 122
    IT_POLICY = 123
    SECURITY_POLICY = 124
    CHANGE_MANAGEMENT = 125
    CONFIGURATION_MANAGEMENT = 126
    RELEASE_MANAGEMENT = 127
    MONITORING = 128
    LOGGING = 129
    PERFORMANCE_MONITORING = 130
    CAPACITY_PLANNING = 131
    SLA_MANAGEMENT = 132
    KPI_TRACKING = 133
    BUDGET_TRACKING = 134
    TIME_TRACKING = 135
    ASSET_MANAGEMENT = 136
    HARDWARE_ASSET = 137
    SOFTWARE_ASSET = 138
    LICENSE_AUDIT = 139
    INCIDENT_TICKETING = 140
    SERVICE_REQUESTS = 141
    PROBLEM_MANAGEMENT = 142
    CHANGE_REQUESTS = 143
    ESCALATIONS = 144
    VULNERABILITY_MANAGEMENT = 145

class ItemEntry:
    def __init__(self, setTeam : int, setPrio : Prio, setType : int, setStatus : dict, setID : int):
        self.team : int = setTeam
        self.priority : Prio = setPrio
        self.itemType : ItemType = setType
        self.statuses : dict = setStatus
        self.curStatus : int = None
        self.itemID : int = setID

        self.content_tag : str = f"t{self.team}p{self.priority.name}ty{self.itemType.name}s"

        self.dataDict : dict = {}

        self.dataDict["Month"] = None
        self.dataDict["Team"] = self.team
        self.dataDict["Priority"] = self.priority.name
        self.dataDict["Type"] = self.itemType.name
        self.dataDict["Status"] = None

        for monthNum in self.statuses.keys():
            if monthNum+1 not in self.statuses:
                self.curStatus = self.statuses[monthNum][len(self.statuses[monthNum])-1]
    
    def __str__(self) -> str:
        output = ("| Item ID: " + str(self.itemID) +
                  " | Teams: " + str(self.team) +
                  " | Priority: " + str(self.priority) +
                  " | Type: " + str(self.itemType) +
                  " | Cur: " + str(self.curStatus))
        return output

    #Returns a dict representing this item's data, optionally at a certain month
    def get_data(self, month = -1) -> dict:
        output : dict = self.dataDict.copy()
        output["Month"] = date_handler.format_date(month)
        output["Status"] = self.statuses[month][len(self.statuses[month])-1].name
        return output

    def produce_content_tag(self, month : int) -> str:
        if month not in self.statuses:
            return "No Tag"
        return "m" + f"{month}{self.content_tag}{self.statuses[month][len(self.statuses[month])-1].name}"
