import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
django.setup()

from app.models import Law

# Laws data to add
laws_to_add = [
    {
        "category": "Property",
        "section_no": "BNS 303",
        "title": "Theft",
        "description": "Theft is the act of taking another person's property without their consent with the intent to deprive them of it.",
        "punishment": "Imprisonment of either description for a term which may extend to three years, or with fine, or with both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Property",
        "section_no": "BNS 308",
        "title": "Extortion",
        "description": "Extortion is the act of intentionally putting any person in fear of any injury to that person or to any other, and thereby dishonestly inducing that person so put in fear to deliver to any person any property or valuable security.",
        "punishment": "Imprisonment of either description for a term which may extend to three years, or with fine, or with both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Magistrate of First Class"
    },
    {
        "category": "Human Body",
        "section_no": "BNS 103",
        "title": "Murder",
        "description": "Culpable homicide is murder if the act by which the death is caused is done with the intention of causing death.",
        "punishment": "Death or imprisonment for life, and shall also be liable to fine.",
        "bailable_status": "Non-Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Court of Session"
    },
    {
        "category": "Human Body",
        "section_no": "BNS 115",
        "title": "Voluntarily causing hurt",
        "description": "Whoever does any act with the intention of thereby causing hurt to any person, or with the knowledge that he is likely thereby to cause hurt to any person, and does thereby cause hurt to any person, is said 'voluntarily to cause hurt'.",
        "punishment": "Imprisonment of either description for a term which may extend to one year, or with fine which may extend to five thousand rupees, or with both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Non-Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Property",
        "section_no": "BNS 316",
        "title": "Criminal breach of trust",
        "description": "Whoever, being in any manner entrusted with property, or with any dominion over property, dishonestly misappropriates or converts to his own use that property.",
        "punishment": "Imprisonment of either description for a term which may extend to three years, or with fine, or with both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Magistrate of First Class"
    },
    {
        "category": "Society",
        "section_no": "BNS 356",
        "title": "Defamation",
        "description": "Whoever, by words either spoken or intended to be read, or by signs or by visible representations, makes or publishes any imputation concerning any person intending to harm, or knowing or having reason to believe that such imputation will harm, the reputation of such person.",
        "punishment": "Simple imprisonment for a term which may extend to two years, or with fine, or with both or with community service.",
        "bailable_status": "Bailable",
        "cognizable_status": "Non-Cognizable",
        "triable_by": "Magistrate of First Class"
    },
    {
        "category": "Human Body",
        "section_no": "BNS 64",
        "title": "Punishment for rape",
        "description": "Whoever commits rape shall be punished with rigorous imprisonment of either description for a term which shall not be less than ten years, but which may extend to imprisonment for life, and shall also be liable to fine.",
        "punishment": "Rigorous imprisonment for 10 years to Life, and fine.",
        "bailable_status": "Non-Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Court of Session"
    },
    {
        "category": "Motor Vehicle",
        "section_no": "Section 185",
        "title": "Drunken Driving",
        "description": "Driving by a drunken person or by a person under the influence of drugs.",
        "punishment": "Imprisonment for a term which may extend to six months, or with fine which may extend to ten thousand rupees, or with both.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Any Magistrate"
    },
    {
        "category": "Cyber Crime",
        "section_no": "Section 66",
        "title": "Computer related offences",
        "description": "If any person, dishonestly or fraudulently, does any act referred to in section 43, he shall be punishable with imprisonment for a term which may extend to three years or with fine which may extend to five lakh rupees or with both.",
        "punishment": "Imprisonment up to 3 years or fine up to 5 lakh rupees.",
        "bailable_status": "Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Magistrate of First Class"
    },
    {
        "category": "Domestic Violence",
        "section_no": "Section 498A",
        "title": "Cruelty by husband or relatives",
        "description": "Whoever, being the husband or the relative of the husband of a woman, subjects such woman to cruelty shall be punished.",
        "punishment": "Imprisonment for a term which may extend to three years and shall also be liable to fine.",
        "bailable_status": "Non-Bailable",
        "cognizable_status": "Cognizable",
        "triable_by": "Magistrate of First Class"
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

print("Done seeding laws.")
