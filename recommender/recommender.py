import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(BASE_DIR, 'csv_file', 'aws_services.csv')
services_df = pd.read_csv(csv_file_path)

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
        "mandatory": ["brand messaging", "brand identity", "media relations", "public", "relation", "public relations", "brand", "strategy", "brand strategy", "brand awareness", "community engagement", "social media strategy", "influencer marketing", "media relations", "press releases", "reputation management"],
        "optional": ["brand awareness", "reputation management", "brand positioning", "press releases",
                     "media coverage", "influencer marketing", "media strategy", "content creation",
                     "storytelling", "social media strategy", "community engagement", "audience", "creating narratives",
                     "enhance", "build reputation", "self-produced communications", "marketing efforts",
                     "face-to-face engagements", "surveys", "blogs", "channels", "feedback", "public relations",
                     "crisis communication", "communication plan", "brand advocacy", "corporate communication",
                     "event management", "media outreach", "press conferences", "media training", "messaging strategy", "consistent messaging", "communication strategy", "business", "identity", "image", "visual identity", "logo design",
                     "recognition", "campaigns", "visibility", "public relation crisis", "reputation repair",
                     "influencer partnerships", "influencer collaborations", "media coverage", "news coverage", "press statements", "media pitching",
                     "narrative building", "audience engagement", "social media content"],
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

def recommend_by_category(category):
    category = category.lower()
    filtered_services = services_df[services_df['Category'].str.lower() == category]
    recommended_services = filtered_services[['Service', 'Use Case']].values.tolist()
    return recommended_services

def recommend_related_services(service_name):
    service_name = service_name.lower()
    service_row = services_df[services_df['Service'].str.lower() == service_name]
    
    if service_row.empty:
        return []
    
    category = service_row['Category'].iloc[0]
    filtered_services = services_df[services_df['Category'].str.lower() == category.lower()]
    
    filtered_services = filtered_services.set_index('Service')
    searched_service = filtered_services.loc[service_row['Service'].values[0]]
    filtered_services = filtered_services.reset_index()
    
    filtered_services = filtered_services[filtered_services['Service'].str.lower() != service_name]
    recommended_services = filtered_services[['Service', 'Use Case']].values.tolist()
    
    recommended_services.insert(0, [searched_service.name, searched_service['Use Case']])
    
    return recommended_services

def handle_user_query(query):
    if query.startswith('category:'):
        category = query.split(':')[1].strip()
        return recommend_by_category(category)
    else:
        service_name = query.strip()
        return recommend_related_services(service_name)


def classify_domains_and_subcategories(user_input):
    user_input = user_input.lower()
    identified_domains = set()
    identified_subcategories = {}

    for domain, details in domain_keywords.items():
        mandatory_keywords = details["mandatory"]
        optional_keywords = details["optional"]
        subcategories = details["Subcategories"]
        
        # Check for at least one mandatory keyword
        has_mandatory = any(keyword.lower() in user_input for keyword in mandatory_keywords)
        
        # Check for any keyword (mandatory or optional) to ensure relevance
        has_any_keyword = any(keyword.lower() in user_input for keyword in mandatory_keywords + optional_keywords)
        
        if has_mandatory and has_any_keyword:
            identified_domains.add(domain)
            identified_subcategories[domain] = [subcat for subcat in subcategories if any(keyword.lower() in user_input for keyword in (mandatory_keywords + optional_keywords))]
    
    return identified_domains, identified_subcategories