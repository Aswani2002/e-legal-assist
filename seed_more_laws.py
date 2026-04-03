import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Law

# More laws to add (focusing on Family, Criminal, Harassment, etc.)
laws_to_add = [
    {
        "category": "Harassment",
        "section_no": "BNS 74",
        "title": "Sexual Harassment",
        "description": "A man committing any of the following acts: physical contact involving unwelcome sexual advances, demand for sexual favors, showing pornography against her will, or making sexually colored remarks.",
        "punishment": "Rigorous imprisonment up to 3 years or fine, or both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Harassment",
        "section_no": "BNS 78",
        "title": "Stalking",
        "description": "Any man who follows a woman and contacts, or attempts to contact such woman to foster personal interaction repeatedly despite a clear indication of disinterest; or monitors the use by a woman of the internet, email or any other form of electronic communication.",
        "punishment": "Imprisonment up to 3 years (first conviction), or 5 years (subsequent).",
        "bailable_status": "Bailable (First offense)",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Criminal",
        "section_no": "NI Act 138",
        "title": "Cheque Bounce",
        "description": "Dishonour of cheque for insufficiency, etc., of funds in the account.",
        "punishment": "Imprisonment for a term which may extend to two years, or with fine which may extend to twice the amount of the cheque, or with both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Non-Cognizable",
        "triable_by": "Judicial Magistrate First Class"
    },
    {
        "category": "Family",
        "section_no": "HMA 13",
        "title": "Divorce",
        "description": "Dissolution of marriage by a decree of divorce on grounds such as adultery, cruelty, desertion, conversion, insanity, leprosy, venereal disease, renunciation, or missing status.",
        "punishment": "Civil Remedy (Decree of Divorce)",
        "bailable_status": "N/A",
        "cognizable_status": "N/A",
        "triable_by": "District Court / Family Court"
    },
    {
        "category": "Family",
        "section_no": "BNS 84",
        "title": "Domestic Violence (Cruelty)",
        "description": "Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty.",
        "punishment": "Imprisonment for a term which may extend to three years and shall also be liable to fine.",
        "bailable_status": "Non-Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Magistrate of First Class"
    },
    {
        "category": "Criminal",
        "section_no": "BNS 303",
        "title": "Theft",
        "description": "Taking property without consent.",
        "punishment": "Imprisonment up to 3 years or fine.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Cyber Crime",
        "section_no": "IT Act 66E",
        "title": "Violation of Privacy",
        "description": "Intentionally capturing, publishing or transmitting the image of a private area of any person without his or her consent.",
        "punishment": "Imprisonment up to 3 years or fine up to 2 lakh rupees, or both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Traffic",
        "section_no": "MVA 184",
        "title": "Dangerous Driving",
        "description": "Driving a motor vehicle in a manner which is dangerous to the public.",
        "punishment": "Imprisonment up to 1 year and/or fine (first offense).",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Family",
        "section_no": "BNS 96",
        "title": "Bigamy",
        "description": "Marrying again during lifetime of husband or wife.",
        "punishment": "Imprisonment up to 7 years and fine.",
        "bailable_status": "Bailable",
        "cognizable_status": "Non-Cognizable",
        "triable_by": "Magistrate of First Class"
    },
    {
        "category": "Harassment",
        "section_no": "POSH Act",
        "title": "Workplace Harassment",
        "description": "Sexual harassment of women at workplace preventing their participation in work and violating their right to a safe environment.",
        "punishment": "Civil/Administrative action + Criminal action under BNS.",
        "bailable_status": "Bailable",
        "cognizable_status": "Non-Cognizable",
        "triable_by": "Local Committee / Internal Committee"
    }
]

for law_data in laws_to_add:
    obj, created = Law.objects.update_or_create(
        section_no=law_data["section_no"],
        defaults=law_data
    )
    if created:
        print(f"Added law: {law_data['title']}")
    else:
        print(f"Updated law: {law_data['title']}")

print("Done seeding additional laws.")
