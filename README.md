## Installation

1. Erstelle ein virtuelles Environment und installiere Abhängigkeiten:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

2. Migrations und Superuser:

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```

3. Server starten:

```bash
python manage.py runserver
```

Frontend: Templates (Bootstrap) sind in `templates/` und ein einfaches Seller-Dashboard ist unter `/seller/dashboard/` verfügbar.

E-Mails laufen aktuell über das Console-Backend (lokaler Test): Emails erscheinen im Terminal.
# Abi-Verkauf

Das Repository beinhaltet eine einfache Django-Webapp, die Vorbestellungen und Lieferungen für Verkäufe an Schulen unterstützt (z. B. Kuchen-Verkauf).

## Features (kurz)
- Rollenbasiertes System: `Kunde`, `Verkäufer`, `Administrator`
- Produkte: Bilder, Beschreibung, Preis, Verfügbarkeit
- Bestellungen: Abholung oder Lieferung (Raumangabe) + Status
- Benachrichtigungen: interne Notifications + E-Mail via Console-Backend

Siehe detaillierte Anleitung im nächsten Abschnitt.