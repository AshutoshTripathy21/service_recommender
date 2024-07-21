from django.test import TestCase
from collections import defaultdict
import os
import csv
# Create your tests here.

domain_keywords = {
    "Cloud": {
        "mandatory": ["cloud", "AWS", "Azure", "Google Cloud","migrate","platform","cloud-based solution", "manage client data", "cloud-based solutions", 
            "IT infrastructure", "telemedicine platform", "data security", 
            "IT systems upgrade", "increased traffic"],
        "optional": ["migrate", "transition", "data migration", "cloud adoption", "cloud architecture",
                     "cloud-native", "microservices", "serverless computing", "IaaS", "PaaS", "SaaS",
                     "virtual machines", "cloud storage", "containerization", "cloud integration",
                     "scalability", "elasticity", "load balancing", "resource optimization", "cost efficiency",
                     "agile deployment", "cloud technologies", "automation", "cloud orchestration",
                     "cloud security", "disaster recovery", "multi-cloud", "hybrid cloud"],
        "Subcategories": [
            "Cloud Strategy Consulting", "Cloud Application Development",
            "Cloud Migration & Integrations", "Increase Capabilities to Scale"
        ]
    },
    "Digital Commerce": {
        "mandatory": [ "e-commerce platform", "recommendation engine", "online store", 
            "customer experience","e-commerce", "digital marketing", "SEO","digital storefront"],
        "optional": ["WooCommerce", "Magento", "web design", "search marketing", "social media management",
                     "customer experience", "personalization", "online sales", "customer journey", 
                     "user experience", "conversion rate optimization", "digital storefront", "payment gateways",
                     "shopping cart", "automation", "web analytics", "product recommendations", "A/B testing",
                     "customer segmentation", "cross-selling", "up-selling", "email marketing", "mobile commerce",
                     "digital transformation", "affiliate marketing", "content management", "supply chain management"],
        "Subcategories": [
            "WooCommerce", "Digital Marketing & Retargetting", 
            "Cloud Services", "General IT Consultation"
        ]
        
    },
    "AI & Analytics": {
        "mandatory": ["financial forecasting", "advanced analytics", "AI", 
            "recommendation", "predictive analytics", "market analysis", 
            "case outcomes", "data analytics", "track","data science", "machine learning", "predictive analytics","AI","model",],
        "optional": ["deep learning", "neural networks", "supervised learning", "unsupervised learning",
                     "reinforcement learning", "data sources", "predictive modeling", "data visualization",
                     "data integration", "big data", "MLOps", "AI chatbot", "conversational AI", "IBM Watson Assistant",
                     "Google Dialogflow", "RASA", "descriptive analytics", "prescriptive analytics", 
                     "anomaly detection", "pattern recognition", "computer vision", "NLP", "data mining",
                     "data analysis", "data governance", "data quality", "data lake", "time series analysis",
                     "clustering", "classification", "regression analysis"],
        "Subcategories": [
            "Image & Document Analysis", "Data Driven Decisions", 
            "Chatbots", "Business Intelligence"
        ]
    },
    "Network Security": {
        "mandatory": ["cybersecurity measures", "threats", "data protection regulations", 
            "data security protocols", "secure data transfers", "high standards","cybersecurity", "firewalls", "encryption"],
        "optional": ["data protection", "endpoint protection", "secure cloud", "SD-WAN", "secure switches",
                     "wireless access points", "VPN", "Zero Trust Access", "network monitoring", "threat detection",
                     "intrusion prevention", "incident response", "vulnerability management", "security compliance",
                     "risk assessment", "DDoS protection", "SIEM", "authentication", "access control",
                     "network segmentation", "security policies", "penetration testing"],
        "Subcategories": [
            "Security Driven Networking", "Adaptive Cloud Security", 
            "Security Operations", "Zero Trust Access"
        ]
    },
    "Process Consulting": {
        "mandatory": ["process optimization", "operational processes", "document management", 
            "compliance","CMMI", "ISO 9001:2015", "Six Sigma"],
        "optional": ["ISO 27001:2013", "process mapping", "process reengineering", "workflow automation",
                     "process efficiency", "business goals", "metrics", "quality management",
                     "operational excellence", "process standardization", "strategic planning", "change management",
                     "business transformation", "performance management", "KPI", "training", "information security",
                     "GDPR", "recommendations", "optimization", "continuous change", "business process improvement",
                     "process benchmarking", "risk management", "compliance management", "organizational development",
                     "project management", "resource allocation", "stakeholder engagement", "process documentation",
                     "process modeling", "business analysis", "best practices"],
        "Subcategories": [
            "Certifications Consulting", "Advisory Services", 
            "Make Changes Happen", "Monitoring & Optimizing"
        ]
    },
    "Learning & Development": {
        "mandatory": [ "employee training", "learning management system (LMS)", 
            "online and offline training","training", "career development", "skill enhancement"],
        "optional": ["upskilling", "reskilling", "technical training", "e-learning", "workshops", "mentoring",
                     "coaching", "blended learning", "interactive learning", "learning management system",
                     "training needs analysis", "training evaluation", "course development", "certified trainers",
                     "simulations", "teamwork", "engaging", "fun", "career consulting", "discovery", "journey",
                     "professional development", "knowledge transfer", "employee training", "talent development",
                     "instructional design", "on-the-job training", "virtual training", "training delivery",
                     "assessment and evaluation"],
        "Subcategories": [
            "Subject Mastery", "Greater Minds Think Further", 
            "Certified Trainers", "Career Consulting"
        ]
        
    },
    "Cyber Risk Advisory": {
        "mandatory": ["cyber risk management", "risk quantification", "data privacy laws", 
            "network security protocols", "secure platform", "privacy regulations","cyber risk management", "risk assessment", "data protection"],
        "optional": ["risk quantification", "risk mitigation", "risk framework", "cyber resilience",
                     "threat intelligence", "incident response planning", "vulnerability assessment", "compliance",
                     "cyber policies", "cyber governance", "security audits", "cyber security", "insights",
                     "informed decisions", "tabletop exercises", "enterprise response", "cyber incident",
                     "third party relationships", "assess", "likelihood", "adapt", "challenges", "opportunities",
                     "cyber risks", "cyber resilience", "threat intelligence", "vulnerability assessment",
                     "business continuity", "disaster recovery", "risk assessment", "security assessment",
                     "penetration testing", "data protection", "information security", "cyber hygiene",
                     "cyber awareness", "cyber policies", "cyber governance", "risk framework", "security architecture",
                     "security controls", "cyber strategy", "risk analysis", "risk appetite", "threat landscape",
                     "security audits"],
        "Subcategories": [
            "Cyber Security Quantification", "Scenario Based Cyber Exercises", 
            "3rd Party Management Review", "Cyber Agility"
        ]
        
    },
    "Talent Resourcing and Management": {
        "mandatory": ["talent acquisition", "recruitment", "hiring strategy"],
        "optional": ["candidate sourcing", "candidate experience", "talent retention", "performance management",
                     "talent development", "succession planning", "HR analytics", "workforce planning",
                     "talent strategy", "remote hiring", "diversity and inclusion", "talent pipeline",
                     "employee branding", "competitive edge", "non-applicants", "applicants", "employees",
                     "employer branding", "job market", "recruitment process", "workforce planning",
                     "talent analytics", "employee engagement", "onboarding", "skill assessment", "recruitment marketing",
                     "job advertising", "candidate screening", "interview process", "employee value proposition",
                     "workforce diversity"],
        "Subcategories": [
            "Sourcing", "Reduce Employee Attrition", "Building a Talent Pipeline", 
            "Improve Business Performance"
        ]
        
    },
    "Customer Communication Management": {
        "mandatory": ["CRM system", "customer engagement", "handle increased customer inquiries","customer journey mapping", "communication strategy", "CRM"],
        "optional": ["multichannel communication", "personalized communication", "customer support", 
                     "customer feedback", "customer service", "automated communication", "customer engagement",
                     "customer satisfaction", "contact center management", "optimizing", "customer experience",
                     "communications workflow", "persuasive force", "desired outcome", "centralized", "standardized",
                     "customer-facing communications", "outbound communication", "avoid problems", "customer interaction",
                     "customer loyalty", "customer insights", "social media communication", "email communication",
                     "messaging apps", "customer relationship", "brand communication", "customer outreach",
                     "service desk", "customer queries", "customer interaction management", "contact center"],
        "Subcategories": [
            "Customer Journey Mapping", "Communications Workflow", 
            "Responsive Customer Driven Communication", "Outbound Communication"
        ]
        
    },
    "Brand Communications & PR": {
        "mandatory": ["brand messaging", "brand identity", "media relations"],
        "optional": ["brand awareness", "reputation management", "brand positioning", "press releases",
                     "media coverage", "influencer marketing", "media strategy", "content creation",
                     "storytelling", "social media strategy", "community engagement", "audience", "creating narratives",
                     "enhance", "build reputation", "self-produced communications", "marketing efforts",
                     "face-to-face engagements", "surveys", "blogs", "channels", "feedback", "public relations",
                     "crisis communication", "communication plan", "brand advocacy", "corporate communication",
                     "event management", "media outreach", "press conferences", "media training"],
         "Subcategories": [
            "Discovering Your Audience", "Storytelling", 
            "Lesser Burn Out", "Public Outreach"
        ]
        
    },
    "Sentiment Analysis & Opinion Mining": {
        "mandatory": [ "sentiment analysis", "opinion mining", "media monitoring", 
            "social listening","sentiment analysis", "social listening", "data analysis"],
        "optional": ["media monitoring", "opinion mining", "content analysis", "social media analytics",
                     "opinion tracking", "trend analysis", "brand monitoring", "natural language processing",
                     "text analysis", "sentiment classification", "emotion detection", "online news", "print",
                     "broadcast", "podcasts", "capturing content", "conversations", "media database",
                     "major markets", "build relationships", "media outreach", "effectiveness", "research",
                     "analyze content", "real-time", "historical access", "social", "editorial conversations",
                     "social publishing", "messages", "schedule", "publish content", "social channel performance",
                     "customer sentiment", "brand sentiment", "market research", "consumer insights",
                     "reputation analysis", "influencer analysis", "opinion dynamics", "topic modeling",
                     "engagement analysis", "brand perception"],
        "Subcategories": [
            "Media Monitoring", "Media Outreach", "Social Listening", 
            "Social Publishing & Engagement"
        ]
        
    },
    "Marketing, Sales Consulting & Strategy": {
        "mandatory": ["marketing strategy", "product launch", "sales and marketing tools", 
            "drive sales","marketing strategy", "sales strategy", "business strategy"],
        "optional": ["go-to-market strategy", "competitive analysis", "optimize sales funnel", "demand generation",
                     "lead generation", "customer acquisition", "marketing analytics", "sales performance analysis",
                     "conversion ratio", "growth strategy", "IT management", "tailored analysis", "technical environment",
                     "functional environment", "plan of action", "strategy", "companies", "skills", "specialist",
                     "support", "sales", "minimize overheads", "marketing plan", "discovering opportunities",
                     "solid strategy", "long term goals", "market research", "competitor analysis", "branding",
                     "product development", "pricing strategy", "distribution strategy", "sales forecasting",
                     "customer retention", "digital marketing strategy", "content strategy", "marketing campaigns",
                     "sales enablement", "channel strategy", "business development", "market positioning",
                     "SWOT analysis", "value proposition", "customer journey mapping", "CRM strategy", "marketing automation"],
        "Subcategories": [
            "IT Management", "Strategy & Support", "Sales", "Marketing Plan"
        ]

    }

}
csv_folder = os.path.join(os.path.dirname(__file__), 'csv_file')
os.makedirs(csv_folder, exist_ok=True)
csv_file = os.path.join(csv_folder, 'domain_keywords.csv')

# Create a CSV file and write the dictionary to it
with open(csv_file, mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the header
    writer.writerow(["Domain", "Mandatory Keywords", "Optional Keywords", "Subcategories"])
    
    # Write the data
    for domain, details in domain_keywords.items():
        mandatory_keywords = ', '.join(details["mandatory"])
        optional_keywords = ', '.join(details["optional"])
        subcategories = ', '.join(details["Subcategories"])
        writer.writerow([domain, mandatory_keywords, optional_keywords, subcategories])

print(f"Data successfully written to {csv_file}")