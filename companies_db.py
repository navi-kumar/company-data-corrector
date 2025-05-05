def get_company_database():
    """
    Returns a database of companies with their information.
    
    In a real application, this would be replaced with API calls
    to services like LinkedIn, Clearbit, or company databases.
    
    Returns:
        dict: Dictionary with company names as keys and company info as values
    """
    return {
        "Google LLC": {
            "industry": "Internet Services and Technology",
            "linkedin": "https://www.linkedin.com/company/google"
        },
        "Apple Inc.": {
            "industry": "Consumer Electronics and Software",
            "linkedin": "https://www.linkedin.com/company/apple"
        },
        "Microsoft Corporation": {
            "industry": "Software and Computing",
            "linkedin": "https://www.linkedin.com/company/microsoft"
        },
        "Amazon.com Inc.": {
            "industry": "E-commerce and Cloud Computing",
            "linkedin": "https://www.linkedin.com/company/amazon"
        },
        "Meta Platforms Inc.": {
            "industry": "Social Media and Technology",
            "linkedin": "https://www.linkedin.com/company/meta"
        },
        "Facebook Inc.": {
            "industry": "Social Media and Technology",
            "linkedin": "https://www.linkedin.com/company/facebook"
        },
        "Tesla Inc.": {
            "industry": "Automotive and Clean Energy",
            "linkedin": "https://www.linkedin.com/company/tesla-motors"
        },
        "Netflix Inc.": {
            "industry": "Entertainment and Streaming Services",
            "linkedin": "https://www.linkedin.com/company/netflix"
        },
        "Intel Corporation": {
            "industry": "Semiconductor Manufacturing",
            "linkedin": "https://www.linkedin.com/company/intel-corporation"
        },
        "IBM Corporation": {
            "industry": "Information Technology and Consulting",
            "linkedin": "https://www.linkedin.com/company/ibm"
        },
        "Adobe Inc.": {
            "industry": "Software and Creative Solutions",
            "linkedin": "https://www.linkedin.com/company/adobe"
        },
        "Oracle Corporation": {
            "industry": "Enterprise Software and Cloud Computing",
            "linkedin": "https://www.linkedin.com/company/oracle"
        },
        "Salesforce Inc.": {
            "industry": "Cloud-based Software",
            "linkedin": "https://www.linkedin.com/company/salesforce"
        },
        "Walmart Inc.": {
            "industry": "Retail and E-commerce",
            "linkedin": "https://www.linkedin.com/company/walmart"
        },
        "JPMorgan Chase & Co.": {
            "industry": "Financial Services and Banking",
            "linkedin": "https://www.linkedin.com/company/jpmorgan-chase"
        },
        "Johnson & Johnson": {
            "industry": "Pharmaceuticals and Consumer Goods",
            "linkedin": "https://www.linkedin.com/company/johnson-&-johnson"
        },
        "Procter & Gamble": {
            "industry": "Consumer Goods",
            "linkedin": "https://www.linkedin.com/company/procter-and-gamble"
        },
        "Coca-Cola Company": {
            "industry": "Beverages",
            "linkedin": "https://www.linkedin.com/company/the-coca-cola-company"
        },
        "PepsiCo Inc.": {
            "industry": "Food and Beverages",
            "linkedin": "https://www.linkedin.com/company/pepsico"
        },
        "Nike Inc.": {
            "industry": "Athletic Apparel and Footwear",
            "linkedin": "https://www.linkedin.com/company/nike"
        },
        "McDonald's Corporation": {
            "industry": "Fast Food and Restaurants",
            "linkedin": "https://www.linkedin.com/company/mcdonald's-corporation"
        },
        "Boeing Company": {
            "industry": "Aerospace and Defense",
            "linkedin": "https://www.linkedin.com/company/boeing"
        },
        "General Electric": {
            "industry": "Conglomerate and Industrial",
            "linkedin": "https://www.linkedin.com/company/ge"
        },
        "Ford Motor Company": {
            "industry": "Automotive",
            "linkedin": "https://www.linkedin.com/company/ford-motor-company"
        },
        "General Motors": {
            "industry": "Automotive",
            "linkedin": "https://www.linkedin.com/company/general-motors"
        },
        "ExxonMobil Corporation": {
            "industry": "Oil and Gas",
            "linkedin": "https://www.linkedin.com/company/exxonmobil"
        },
        "Chevron Corporation": {
            "industry": "Oil and Gas",
            "linkedin": "https://www.linkedin.com/company/chevron"
        },
        "AT&T Inc.": {
            "industry": "Telecommunications",
            "linkedin": "https://www.linkedin.com/company/at&t"
        },
        "Verizon Communications": {
            "industry": "Telecommunications",
            "linkedin": "https://www.linkedin.com/company/verizon"
        },
        "Comcast Corporation": {
            "industry": "Telecommunications and Media",
            "linkedin": "https://www.linkedin.com/company/comcast"
        },
        "Walt Disney Company": {
            "industry": "Entertainment and Media",
            "linkedin": "https://www.linkedin.com/company/the-walt-disney-company"
        },
        "PayPal Holdings Inc.": {
            "industry": "Financial Technology",
            "linkedin": "https://www.linkedin.com/company/paypal"
        },
        "Mastercard Incorporated": {
            "industry": "Financial Services",
            "linkedin": "https://www.linkedin.com/company/mastercard"
        },
        "Visa Inc.": {
            "industry": "Financial Services",
            "linkedin": "https://www.linkedin.com/company/visa"
        },
        "Pfizer Inc.": {
            "industry": "Pharmaceuticals",
            "linkedin": "https://www.linkedin.com/company/pfizer"
        },
        "Merck & Co.": {
            "industry": "Pharmaceuticals",
            "linkedin": "https://www.linkedin.com/company/merck"
        },
        "UnitedHealth Group": {
            "industry": "Healthcare",
            "linkedin": "https://www.linkedin.com/company/unitedhealth-group"
        },
        "CVS Health": {
            "industry": "Healthcare and Retail Pharmacy",
            "linkedin": "https://www.linkedin.com/company/cvs-health"
        },
        "Target Corporation": {
            "industry": "Retail",
            "linkedin": "https://www.linkedin.com/company/target"
        },
        "Home Depot Inc.": {
            "industry": "Home Improvement Retail",
            "linkedin": "https://www.linkedin.com/company/the-home-depot"
        },
        "Lowe's Companies": {
            "industry": "Home Improvement Retail",
            "linkedin": "https://www.linkedin.com/company/lowe's"
        },
        "Starbucks Corporation": {
            "industry": "Coffee and Quick Service Restaurants",
            "linkedin": "https://www.linkedin.com/company/starbucks"
        },
        "Cisco Systems Inc.": {
            "industry": "Networking Technology",
            "linkedin": "https://www.linkedin.com/company/cisco"
        },
        "Accenture plc": {
            "industry": "Professional Services and Technology Consulting",
            "linkedin": "https://www.linkedin.com/company/accenture"
        },
        "Deloitte": {
            "industry": "Professional Services",
            "linkedin": "https://www.linkedin.com/company/deloitte"
        },
        "PwC (PricewaterhouseCoopers)": {
            "industry": "Professional Services",
            "linkedin": "https://www.linkedin.com/company/pwc"
        },
        "Ernst & Young (EY)": {
            "industry": "Professional Services",
            "linkedin": "https://www.linkedin.com/company/ernst-&-young"
        },
        "KPMG": {
            "industry": "Professional Services",
            "linkedin": "https://www.linkedin.com/company/kpmg"
        },
        "McKinsey & Company": {
            "industry": "Management Consulting",
            "linkedin": "https://www.linkedin.com/company/mckinsey-&-company"
        },
        "Boston Consulting Group (BCG)": {
            "industry": "Management Consulting",
            "linkedin": "https://www.linkedin.com/company/boston-consulting-group"
        },
        "Bain & Company": {
            "industry": "Management Consulting",
            "linkedin": "https://www.linkedin.com/company/bain-&-company"
        },
        "Goldman Sachs": {
            "industry": "Financial Services and Investment Banking",
            "linkedin": "https://www.linkedin.com/company/goldman-sachs"
        },
        "Morgan Stanley": {
            "industry": "Financial Services and Investment Banking",
            "linkedin": "https://www.linkedin.com/company/morgan-stanley"
        },
        "BlackRock Inc.": {
            "industry": "Asset Management",
            "linkedin": "https://www.linkedin.com/company/blackrock"
        },
        "Airbnb Inc.": {
            "industry": "Travel and Hospitality Technology",
            "linkedin": "https://www.linkedin.com/company/airbnb"
        },
        "Uber Technologies Inc.": {
            "industry": "Transportation Technology",
            "linkedin": "https://www.linkedin.com/company/uber-com"
        },
        "Lyft Inc.": {
            "industry": "Transportation Technology",
            "linkedin": "https://www.linkedin.com/company/lyft"
        },
        "DoorDash Inc.": {
            "industry": "Food Delivery Technology",
            "linkedin": "https://www.linkedin.com/company/doordash"
        },
        "Spotify Technology": {
            "industry": "Music Streaming",
            "linkedin": "https://www.linkedin.com/company/spotify"
        },
        "Twitter Inc.": {
            "industry": "Social Media",
            "linkedin": "https://www.linkedin.com/company/twitter"
        },
        "Snapchat Inc.": {
            "industry": "Social Media",
            "linkedin": "https://www.linkedin.com/company/snap-inc"
        },
        "Pinterest Inc.": {
            "industry": "Social Media",
            "linkedin": "https://www.linkedin.com/company/pinterest"
        },
        "LinkedIn Corporation": {
            "industry": "Professional Networking and Social Media",
            "linkedin": "https://www.linkedin.com/company/linkedin"
        },
        "Zoom Video Communications": {
            "industry": "Video Conferencing Technology",
            "linkedin": "https://www.linkedin.com/company/zoom-video-communications"
        },
        "Slack Technologies": {
            "industry": "Business Communication Technology",
            "linkedin": "https://www.linkedin.com/company/slack-technologies"
        },
        "Shopify Inc.": {
            "industry": "E-commerce Platform",
            "linkedin": "https://www.linkedin.com/company/shopify"
        },
        "Palantir Technologies": {
            "industry": "Data Analytics and Software",
            "linkedin": "https://www.linkedin.com/company/palantir-technologies"
        },
        "SpaceX": {
            "industry": "Aerospace Manufacturing and Space Transportation",
            "linkedin": "https://www.linkedin.com/company/spacex"
        },
        "Samsung Electronics": {
            "industry": "Consumer Electronics and Technology",
            "linkedin": "https://www.linkedin.com/company/samsung-electronics"
        },
        "Sony Corporation": {
            "industry": "Consumer Electronics and Entertainment",
            "linkedin": "https://www.linkedin.com/company/sony"
        },
        "LG Electronics": {
            "industry": "Consumer Electronics",
            "linkedin": "https://www.linkedin.com/company/lg-electronics"
        },
        "HP Inc.": {
            "industry": "Information Technology and Hardware",
            "linkedin": "https://www.linkedin.com/company/hp"
        },
        "Dell Technologies": {
            "industry": "Information Technology and Hardware",
            "linkedin": "https://www.linkedin.com/company/delltechnologies"
        },
        "Lenovo Group": {
            "industry": "Information Technology and Hardware",
            "linkedin": "https://www.linkedin.com/company/lenovo"
        },
        "NVIDIA Corporation": {
            "industry": "Semiconductor Technology",
            "linkedin": "https://www.linkedin.com/company/nvidia"
        },
        "Advanced Micro Devices (AMD)": {
            "industry": "Semiconductor Technology",
            "linkedin": "https://www.linkedin.com/company/amd"
        },
        "Qualcomm Inc.": {
            "industry": "Semiconductor Technology",
            "linkedin": "https://www.linkedin.com/company/qualcomm"
        },
        "Texas Instruments": {
            "industry": "Semiconductor Technology",
            "linkedin": "https://www.linkedin.com/company/texas-instruments"
        },
        "Ericsson": {
            "industry": "Telecommunications Equipment",
            "linkedin": "https://www.linkedin.com/company/ericsson"
        },
        "Nokia Corporation": {
            "industry": "Telecommunications Equipment",
            "linkedin": "https://www.linkedin.com/company/nokia"
        },
        "Siemens AG": {
            "industry": "Industrial Manufacturing and Technology",
            "linkedin": "https://www.linkedin.com/company/siemens"
        },
        "Philips": {
            "industry": "Health Technology and Consumer Electronics",
            "linkedin": "https://www.linkedin.com/company/philips"
        },
        "Panasonic Corporation": {
            "industry": "Consumer Electronics",
            "linkedin": "https://www.linkedin.com/company/panasonic"
        },
        "BMW Group": {
            "industry": "Automotive",
            "linkedin": "https://www.linkedin.com/company/bmw-group"
        },
        "Toyota Motor Corporation": {
            "industry": "Automotive",
            "linkedin": "https://www.linkedin.com/company/toyota-motor-corporation"
        },
        "Volkswagen Group": {
            "industry": "Automotive",
            "linkedin": "https://www.linkedin.com/company/volkswagen-group"
        },
        "Nestlé S.A.": {
            "industry": "Food and Beverage",
            "linkedin": "https://www.linkedin.com/company/nestle-s-a-"
        },
        "Unilever": {
            "industry": "Consumer Goods",
            "linkedin": "https://www.linkedin.com/company/unilever"
        },
        "L'Oréal": {
            "industry": "Cosmetics and Beauty",
            "linkedin": "https://www.linkedin.com/company/loreal"
        },
        "Adidas AG": {
            "industry": "Athletic Apparel and Footwear",
            "linkedin": "https://www.linkedin.com/company/adidas"
        },
        "H&M Group": {
            "industry": "Retail and Fashion",
            "linkedin": "https://www.linkedin.com/company/h&m"
        },
        "IKEA": {
            "industry": "Furniture Retail",
            "linkedin": "https://www.linkedin.com/company/ikea"
        },
        "Novartis International AG": {
            "industry": "Pharmaceuticals",
            "linkedin": "https://www.linkedin.com/company/novartis"
        },
        "Roche Holding AG": {
            "industry": "Pharmaceuticals and Diagnostics",
            "linkedin": "https://www.linkedin.com/company/roche"
        },
        "AstraZeneca plc": {
            "industry": "Pharmaceuticals",
            "linkedin": "https://www.linkedin.com/company/astrazeneca"
        },
        "GlaxoSmithKline (GSK)": {
            "industry": "Pharmaceuticals",
            "linkedin": "https://www.linkedin.com/company/glaxosmithkline"
        }
    }
