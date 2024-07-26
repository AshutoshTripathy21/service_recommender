import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(BASE_DIR, 'csv_file', 'aws_services.csv')
services_df = pd.read_csv(csv_file_path)

domain_keywords = {
    "Cloud": {
        "mandatory": ["cloud", "AWS", "Azure", "Google Cloud", "migrate", "platform", "cloud-based solution", 
                      "manage client data", "cloud-based solutions", "IT infrastructure", "telemedicine platform", 
                      "data security", "IT systems upgrade", "increased traffic", "cloud computing", 
                      "cloud deployment", "cloud service providers", "data center", "cloud infrastructure", 
                      "cloud management", "cloud optimization", "public cloud", "private cloud", "cloud readiness", "fault tolerance", "database"],
        "optional": ["migrate", "transition", "data migration", "cloud adoption", "cloud architecture", 
                     "cloud-native", "microservices", "serverless computing", "IaaS", "PaaS", "SaaS", 
                     "virtual machines", "cloud storage", "containerization", "cloud integration", "scalability", 
                     "elasticity", "load balancing", "resource optimization", "cost efficiency", "agile deployment", 
                     "cloud technologies", "automation", "cloud orchestration", "cloud security", "disaster recovery", 
                     "multi-cloud", "hybrid cloud", "cloud automation", "cloud consulting", "cloud cost management", 
                     "cloud operations", "cloud performance", "cloud platforms", "cloud services", "cloud storage solutions", 
                     "cloud strategy", "cloud transformation", "seamless"],
        "Subcategories": ["Cloud Strategy Consulting", "Cloud Application Development", "Cloud Migration & Integrations", 
                          "Increase Capabilities to Scale"]
    },
    "Digital Commerce": {
        "mandatory": ["e-commerce platform", "recommendation engine", "online store", "customer experience", 
                      "e-commerce", "digital marketing", "SEO", "digital storefront", "digital marketplace", 
                      "shopping experience", "online retail", "product listings", "customer reviews", "checkout process", 
                      "inventory management", "e-commerce analytics", "digital storefront", "mobile commerce"],
        "optional": ["WooCommerce", "Magento", "web design", "search marketing", "social media management", 
                     "customer experience", "personalization", "online sales", "customer journey", "user experience", 
                     "conversion rate optimization", "digital storefront", "payment gateways", "shopping cart", 
                     "automation", "web analytics", "product recommendations", "A/B testing", "customer segmentation", 
                     "cross-selling", "up-selling", "email marketing", "mobile commerce", "digital transformation", 
                     "affiliate marketing", "content management", "supply chain management", "e-commerce security", 
                     "customer retention strategies", "multi-channel selling", "online advertising", "e-commerce integration", 
                     "online payment processing", "sales optimization", "e-commerce SEO", "shopping cart abandonment", 
                     "e-commerce trends"],
        "Subcategories": ["WooCommerce", "Digital Marketing & Retargetting", "Cloud Services", "General IT Consultation"]
    },
    "AI & Analytics": {
        "mandatory": ["financial forecasting", "advanced analytics", "AI", "recommendation", "predictive analytics", 
                      "market analysis", "case outcomes", "data analytics", "track", "data science", "machine learning", 
                      "predictive analytics", "AI", "model", "data modeling", "predictive maintenance", "AI solutions", 
                      "data-driven insights", "AI algorithms", "data processing", "AI integration", "business analytics", 
                      "data science project", "AI implementation"],
        "optional": ["deep learning", "neural networks", "supervised learning", "unsupervised learning", 
                     "reinforcement learning", "data sources", "predictive modeling", "data visualization", 
                     "data integration", "big data", "MLOps", "AI chatbot", "conversational AI", "IBM Watson Assistant", 
                     "Google Dialogflow", "RASA", "descriptive analytics", "prescriptive analytics", "anomaly detection", 
                     "pattern recognition", "computer vision", "NLP", "data mining", "data analysis", "data governance", 
                     "data quality", "data lake", "time series analysis", "clustering", "classification", "regression analysis", 
                     "predictive insights", "data science frameworks", "machine learning models", "AI-powered applications", 
                     "real-time analytics", "big data analytics", "data science platforms", "AI research", "automated machine learning", 
                     "AI data pipelines"],
        "Subcategories": ["Image & Document Analysis", "Data Driven Decisions", "Chatbots", "Business Intelligence"]
    },
    "Network Security": {
        "mandatory": ["cybersecurity measures", "threats", "data protection regulations", "data security protocols", 
                      "secure data transfers", "high standards", "cybersecurity", "firewalls", "encryption", 
                      "network security policies", "cyber threats", "data loss prevention", "security infrastructure", 
                      "network defense", "secure communication", "security breaches", "data encryption standards", 
                      "network vulnerabilities", "security monitoring"],
        "optional": ["data protection", "endpoint protection", "secure cloud", "SD-WAN", "secure switches", 
                     "wireless access points", "VPN", "Zero Trust Access", "network monitoring", "threat detection", 
                     "intrusion prevention", "incident response", "vulnerability management", "security compliance", 
                     "risk assessment", "DDoS protection", "SIEM", "authentication", "access control", "network segmentation", 
                     "security policies", "penetration testing", "identity management", "network access control", 
                     "security incident management", "threat response", "data encryption protocols", "network security architecture", 
                     "cyber defense strategies", "network security standards", "network security assessments", "data integrity"],
        "Subcategories": ["Security Driven Networking", "Adaptive Cloud Security", "Security Operations", "Zero Trust Access"]
    },
    "Process Consulting": {
        "mandatory": ["process optimization", "operational processes", "document management", "compliance", "CMMI", 
                      "ISO 9001:2015", "Six Sigma", "business process optimization", "process improvement", 
                      "efficiency enhancement", "process redesign", "quality assurance", "business process management", 
                      "workflow improvement", "operational strategy", "process automation", "organizational efficiency"],
        "optional": ["ISO 27001:2013", "process mapping", "process reengineering", "workflow automation", 
                     "process efficiency", "business goals", "metrics", "quality management", "operational excellence", 
                     "process standardization", "strategic planning", "change management", "business transformation", 
                     "performance management", "KPI", "training", "information security", "GDPR", "recommendations", 
                     "optimization", "continuous change", "business process improvement", "process benchmarking", 
                     "risk management", "compliance management", "organizational development", "project management", 
                     "resource allocation", "stakeholder engagement", "process documentation", "process modeling", 
                     "business analysis", "best practices", "process analytics", "process assessment", "process documentation", 
                     "performance improvement", "business process modeling", "continuous improvement", "operational strategy", 
                     "process execution", "business process redesign", "process frameworks"],
        "Subcategories": ["Certifications Consulting", "Advisory Services", "Make Changes Happen", "Monitoring & Optimizing"]
    },
    "Learning & Development": {
        "mandatory": ["employee training", "learning management system (LMS)", "online and offline training", "training", 
                      "career development", "skill enhancement", "skill development", "employee growth", "training programs", 
                      "learning solutions", "educational resources", "knowledge enhancement", "professional training", 
                      "career advancement", "learning initiatives", "development programs"],
        "optional": ["upskilling", "reskilling", "technical training", "e-learning", "workshops", "mentoring", "coaching", 
                     "blended learning", "interactive learning", "learning management system", "training needs analysis", 
                     "training evaluation", "course development", "certified trainers", "simulations", "teamwork", "engaging", 
                     "fun", "career consulting", "discovery", "journey", "professional development", "knowledge transfer", 
                     "employee training", "talent development", "instructional design", "on-the-job training", "virtual training", 
                     "training delivery", "assessment and evaluation", "employee engagement", "learning technologies", 
                     "learning platforms", "talent development programs", "employee onboarding", "learning strategies", 
                     "training delivery", "instructional methodologies", "learning resources", "development frameworks"],
        "Subcategories": ["Subject Mastery", "Greater Minds Think Further", "Certified Trainers", "Career Consulting"]
    },
    "Cyber Risk Advisory": {
        "mandatory": ["cyber risk management", "risk quantification", "data privacy laws", "network security protocols", 
                      "secure platform", "privacy regulations", "cyber risk management", "risk assessment", "data protection", 
                      "cyber risk assessment", "cyber risk framework", "cyber threat landscape", "data protection strategies", 
                      "cyber risk evaluation", "risk management protocols", "cyber risk advisory", "data security measures", 
                      "cyber incident response", "cyber risk mitigation"],
        "optional": ["risk analytics", "regulatory compliance", "data privacy", "security audit", "third-party risk", 
                     "cyber hygiene", "business continuity", "emerging risks", "threat intelligence", "risk dashboard", 
                     "data breaches", "security frameworks", "business resilience", "crisis management", "cyber insurance", 
                     "incident management", "privacy impact assessment", "vendor risk management", "risk appetite", 
                     "data governance", "ISO/IEC 27001", "NIST framework", "GDPR compliance", "PCI-DSS compliance", 
                     "risk policies", "cyber risk analytics", "threat assessment", "cyber resilience strategies", 
                     "data breach prevention", "risk management strategies", "cyber risk governance", "cyber security measures", 
                     "risk identification", "cyber risk planning"],
        "Subcategories": ["Plan & Strategize", "Security & Control", "Risk Management", "Data Driven Solutions"]
    },
    "Talent Resourcing and Management": {
        "mandatory": ["recruitment process", "talent acquisition", "job portal", "talent sourcing", "recruitment", 
                      "talent management", "workforce planning", "recruitment strategy", "talent acquisition process", 
                      "employee retention", "talent pipeline management", "recruitment campaigns", "talent sourcing strategies", 
                      "workforce optimization", "employee onboarding process"],
        "optional": ["onboarding", "talent search", "candidate sourcing", "staffing", "headhunting", "interview process", 
                     "talent pool", "candidate selection", "talent retention", "employee engagement", "HR strategy", 
                     "employee development", "job market analysis", "talent analytics", "HR technology", "workforce diversity", 
                     "talent development", "succession planning", "performance management", "employee benefits", 
                     "HR compliance", "recruitment analytics", "talent development programs", "recruitment strategies", 
                     "candidate engagement", "talent assessment", "human capital management", "employee performance", 
                     "talent retention strategies", "workforce analytics", "candidate experience management"],
        "Subcategories": ["Search & Selection", "Volume Hiring", "Recruitment Marketing", "Talent Management"]
    },
    "Customer Communication Management": {
        "mandatory": ["customer service", "inquiries", "customer communication channels", "CRM", "communication", 
                      "client management", "customer communication strategy", "customer interaction", "customer relationship management", 
                      "customer service protocols", "customer engagement platforms", "CRM solutions", "customer inquiry handling", 
                      "customer support strategy", "customer satisfaction management", "customer communication tools"],
        "optional": ["email support", "phone support", "chat support", "social media support", "customer feedback", 
                     "customer feedback management", "customer communication optimization", "customer relationship strategies", 
                     "customer communication platforms", "customer interaction management", "customer service workflows", 
                     "self-service portals", "ticketing system", "communication automation", "customer outreach", 
                     "customer follow-up", "customer retention", "customer loyalty", "customer surveys", "support ticketing", 
                     "customer response time", "customer service metrics", "omnichannel support", "support analytics", 
                     "communication software", "live chat", "helpdesk", "customer engagement", "customer onboarding", 
                     "CRM integration", "customer service enhancement", "multichannel customer support", 
                     "customer communication optimization", "customer interaction management", "customer service workflows"],
        "Subcategories": ["Dynamic Communications", "Platform Expertise", "Digital Transformation", "Customer Experience"]
    },
    "Brand Communications & PR": {
        "mandatory": ["brand strategy", "media relations", "publicity", "crisis management", "PR", "brand communications", 
                      "media outreach", "public relations strategy", "brand communication", "reputation building", 
                      "brand positioning", "media engagement", "PR campaigns", "brand storytelling", "crisis communication"],
        "optional": ["press releases", "media kits", "public statements", "crisis response", "brand reputation", 
                     "media coverage", "public image", "media partnerships", "media outreach", "branding", "media events", 
                     "PR strategy", "social media PR", "media training", "press conferences", "brand consistency", 
                     "public relations metrics", "brand visibility", "PR tactics", "brand enhancement", 
                     "media relations management", "public engagement", "brand advocacy", "media pitching", 
                     "brand influence", "public perception management"],
        "Subcategories": ["Brand Strategy", "Public Relations", "Content Management", "Media Outreach"]
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