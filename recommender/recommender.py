import pandas as pd
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

csv_file_path = os.path.join(BASE_DIR, 'csv_file', 'aws_services.csv')
services_df = pd.read_csv(csv_file_path)

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
