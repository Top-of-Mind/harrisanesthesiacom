import json
import os

# Generates every HTML page and sitemap.xml. Edit content here, then run: python tools/build_site.py
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://harrisanesthesia.com"
PHONE_HREF = "tel:+16507059152"
PHONE = "(650) 705-9152"
EMAIL = "info@harrisanesthesia.com"
RATE_SHEET = "mailto:info@harrisanesthesia.com?subject=Request%20Rate%20Sheet"

CITIES = [
    ("austin", "Austin"),
    ("houston", "Houston"),
    ("dallas", "Dallas"),
    ("san-antonio", "San Antonio"),
]
SERVICES = [
    ("pediatric-dental-anesthesia", "Pediatric Dentistry"),
    ("oral-surgery-anesthesia", "Oral &amp; Maxillofacial Surgery"),
    ("periodontal-surgery-anesthesia", "Periodontics"),
    ("full-arch-implant-anesthesia", "Full-Arch &amp; Advanced Implants"),
    ("general-cosmetic-dental-anesthesia", "General &amp; Cosmetic Dentistry"),
]

TESTIMONIALS = {
    "gonzalez": {
        "quote": "Brett is the best anesthesiologist I have worked with, and as an oral and maxillofacial surgeon I know quality when I see it.",
        "name": "Dr. Juan Gonzalez, DMD, OMS",
        "role": "Board-Certified Oral &amp; Maxillofacial Surgeon",
        "link": ("https://infiniadental.com/dr-juan-gonzalez/", "Profile"),
        "place": "Round Rock, TX",
        "social": ("https://www.instagram.com/dr.g.dmd.omfs", "@dr.g.dmd.omfs"),
    },
    "chung": {
        "quote": "Dr. Harris is a pleasure to work with and we absolutely trust him to take care of our patients under anesthesia. From pediatric to medically compromised elderly patients, and everyone in between, Dr. Harris is our go-to for in-office anesthesia for procedures ranging from general and cosmetic dentistry to the full scope of oral and maxillofacial surgery!",
        "name": "Dr. Madeleine Chung, DDS",
        "role": "Austin Cosmetic &amp; Implant Dentistry",
        "link": ("https://austintopdentist.com/", "austintopdentist.com"),
        "place": "Austin, TX",
        "social": ("https://www.instagram.com/drmadeleinechung/", "@drmadeleinechung"),
    },
    "friedberg": {
        "quote": "I&rsquo;ve worked with multiple anesthesiologists over my 25 year career. Dr. Harris is hands down the best to work with. He is excellent technically, great with patients and staff &mdash; if I can&rsquo;t work with him, the case gets delayed.",
        "name": "Dr. Robert Friedberg, DMD",
        "role": "Board-Certified Periodontist, J. Robert Friedberg, DMD &amp; Associates",
        "link": ("https://drfriedbergandassociates.com/", "drfriedbergandassociates.com"),
        "place": "Houston, TX",
        "social": ("https://www.instagram.com/dr.friedberg_/", "@dr.friedberg_"),
    },
}

HOW_STEPS = [
    ("Book a Date", "Call, email, or use the form to schedule Dr. Harris around your existing surgical calendar."),
    ("Share the Patient&rsquo;s History", "Send the patient&rsquo;s health history ahead of the appointment so Dr. Harris can plan the anesthesia."),
    ("Dr. Harris Arrives Ready", "He brings his own anesthesia, monitoring, and emergency equipment, manages the case, and stays until your patient meets discharge criteria."),
]

WHY_POINTS = [
    "Accountable to the same dental board as your practice",
    "Stays with your patient until discharge criteria are met",
    "Brings his own anesthesia, monitoring, and emergency equipment",
    "One flat fee per case, billed directly to your practice",
    "Mobile dental anesthesia is his full-time practice",
]


def testimonial_figure(key):
    t = TESTIMONIALS[key]
    return f"""        <figure class="testimonial">
          <blockquote>&ldquo;{t['quote']}&rdquo;</blockquote>
          <figcaption>
            <span class="testimonial-name">{t['name']}</span>
            <span class="testimonial-role">{t['role']}</span>
            <span class="testimonial-place"><a href="{t['link'][0]}" target="_blank" rel="noopener">{t['link'][1]}</a> &middot; {t['place']}</span>
            <a class="testimonial-social" href="{t['social'][0]}" target="_blank" rel="noopener">{t['social'][1]}</a>
          </figcaption>
        </figure>"""


def how_steps_html():
    items = "\n".join(
        f"""          <li class="how-step"><span class="how-num">{i}</span><h4>{title}</h4><p>{body}</p></li>"""
        for i, (title, body) in enumerate(HOW_STEPS, 1)
    )
    return f"""        <ol class="how-steps">
{items}
        </ol>"""


def head(title, description, path, extra=""):
    url = SITE + path
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:image" content="{SITE}/assets/dr-harris-headshot-crop.jpg">
<link rel="icon" type="image/png" href="/assets/logo-icon.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/css/styles.css">
{extra}</head>
<body>

<div class="topbar">
  <div class="wrap topbar-inner">
    <span>Mobile Dental Anesthesia for Practices Across the Texas Triangle</span>
    <a href="{PHONE_HREF}" class="topbar-phone">{PHONE}</a>
  </div>
</div>

<header class="site-header" id="top">
  <div class="wrap header-inner">
    <a href="/" class="brand">
      <img src="/assets/logo-icon.png" alt="Harris Anesthesia Group mark" class="brand-mark">
      <span class="brand-word">
        <span class="brand-name">HARRIS</span>
        <span class="brand-sub">Anesthesia Group</span>
      </span>
    </a>
    <nav class="site-nav" id="site-nav">
      <a href="/#services">Services</a>
      <a href="/#how-it-works">How It Works</a>
      <a href="/#why">Why Us</a>
      <a href="/#about">About</a>
      <a href="/#faq">FAQ</a>
    </nav>
    <a href="/#contact" class="btn btn-primary header-cta">Book Dr. Harris</a>
    <button class="nav-toggle" id="nav-toggle" aria-label="Toggle navigation" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
"""


def footer():
    city_links = "\n".join(f'          <li><a href="/{slug}/">{name}, TX</a></li>' for slug, name in CITIES)
    service_links = "\n".join(f'          <li><a href="/{slug}/">{name}</a></li>' for slug, name in SERVICES)
    return f"""
<footer class="site-footer">
  <div class="wrap footer-cols">
    <div class="footer-brand-col">
      <a href="/" class="brand brand-footer">
        <img src="/assets/logo-icon.png" alt="Harris Anesthesia Group mark" class="brand-mark">
        <span class="brand-word">
          <span class="brand-name">HARRIS</span>
          <span class="brand-sub">Anesthesia Group</span>
        </span>
      </a>
      <p class="footer-tagline">Mobile dental anesthesia for practices across the Texas Triangle.</p>
      <p class="footer-contact"><a href="{PHONE_HREF}">{PHONE}</a><br><a href="mailto:{EMAIL}">{EMAIL}</a></p>
    </div>
    <div>
      <h4 class="footer-heading">Service Areas</h4>
      <ul class="footer-links">
{city_links}
      </ul>
    </div>
    <div>
      <h4 class="footer-heading">Services</h4>
      <ul class="footer-links">
{service_links}
      </ul>
    </div>
  </div>
  <p class="footer-copy">&copy; <span id="year"></span> Harris Anesthesia Group. All rights reserved.</p>
</footer>

<script src="/js/main.js"></script>
</body>
</html>
"""


def write(path, html):
    full = os.path.join(ROOT, path)
    os.makedirs(os.path.dirname(full), exist_ok=True)
    with open(full, "w", encoding="utf-8", newline="\n") as f:
        f.write(html)


# ---------------------------------------------------------------- home page

LD = {
    "@context": "https://schema.org",
    "@type": "MedicalBusiness",
    "name": "Harris Anesthesia Group",
    "url": SITE + "/",
    "logo": SITE + "/assets/logo-icon.png",
    "image": SITE + "/assets/dr-harris-headshot-crop.jpg",
    "description": "Mobile dental anesthesiology practice providing office-based general anesthesia for dental practices across the Texas Triangle.",
    "telephone": "+1-650-705-9152",
    "email": EMAIL,
    "medicalSpecialty": "Anesthesia",
    "areaServed": [{"@type": "City", "name": f"{name}, TX"} for _, name in CITIES],
    "founder": {
        "@type": "Person",
        "name": "Brett Harris",
        "honorificSuffix": "DMD",
        "jobTitle": "Dental Anesthesiologist",
        "alumniOf": [
            {"@type": "CollegeOrUniversity", "name": "University of Nevada, Las Vegas School of Dental Medicine"},
            {"@type": "Organization", "name": "NYU Langone Hospitals"},
            {"@type": "CollegeOrUniversity", "name": "Brigham Young University"},
        ],
    },
}
ld_script = '<script type="application/ld+json">\n' + json.dumps(LD, indent=2) + "\n</script>\n"

service_card_text = {
    "pediatric-dental-anesthesia": "Children who need general anesthesia to complete treatment safely, in your own office instead of a hospital operating room.",
    "oral-surgery-anesthesia": "Extractions, third molars, grafting, and the other surgical cases your practice lines up for general anesthesia.",
    "periodontal-surgery-anesthesia": "Periodontal and implant surgery performed with a secured airway, start to finish.",
    "full-arch-implant-anesthesia": "All-on-X, zygomatic and pterygoid implants, full-arch placement with sinus lifts, full-mouth extractions with immediate implants, alveoloplasty, and bone block grafting.",
    "general-cosmetic-dental-anesthesia": "Extensive restorative and cosmetic treatment, and anxious patients who are best treated in a single visit under anesthesia.",
}
service_cards = "\n".join(
    f"""        <a class="service-card" href="/{slug}/">
          <span class="service-index">{i:02d}</span>
          <h3>{name}</h3>
          <p>{service_card_text[slug]}</p>
          <span class="card-link">Learn more &rarr;</span>
        </a>"""
    for i, (slug, name) in enumerate(SERVICES, 1)
)

FAQ = [
    ("Where does Dr. Harris work?",
     "Anywhere in the Texas Triangle &mdash; Austin, San Antonio, Houston, Dallas, and the surrounding communities. He comes to your office; your patients never leave your practice."),
    ("How is anesthesia billed?",
     f"One flat fee per case, billed directly to your practice &mdash; there&rsquo;s no separate patient billing for your team to manage. <a href=\"{RATE_SHEET}\">Email us for our current rate sheet.</a>"),
    ("Do we need to buy anesthesia equipment?",
     "Dr. Harris brings his own anesthesia, monitoring, and emergency equipment to every case, so your practice doesn&rsquo;t need to purchase or maintain it."),
    ("What kinds of practices do you work with?",
     "Pediatric dentists, oral and maxillofacial surgeons, periodontists, prosthodontists and implant practices, and general and cosmetic dentists."),
    ("We already have an anesthesia provider, or do our own sedation. Can we still work with you?",
     "Yes. Many practices work with more than one anesthesia provider. Keep Dr. Harris on call for cases that need general anesthesia and for the days your usual provider is booked."),
    ("Does Dr. Harris stay until the patient recovers?",
     "Yes. He monitors every patient through emergence and recovery, and stays until discharge criteria are met."),
    ("How do we get started?",
     f"Call <a href=\"{PHONE_HREF}\">{PHONE}</a>, email <a href=\"mailto:{EMAIL}\">{EMAIL}</a>, or use the form below with your practice name, city, and the type of cases you&rsquo;d like covered."),
]
faq_html = "\n".join(
    f"""        <details class="faq-item">
          <summary>{q}</summary>
          <p>{a}</p>
        </details>"""
    for q, a in FAQ
)

home = head(
    "Mobile Dental Anesthesiologist in Texas | Harris Anesthesia Group",
    "Dr. Brett Harris brings office-based general anesthesia to dental practices in Austin, Houston, Dallas &amp; San Antonio. One flat fee per case.",
    "/",
    ld_script,
) + f"""
<main>

  <section class="hero">
    <div class="wrap hero-inner">
      <p class="eyebrow">Austin &middot; Houston &middot; Dallas &middot; San Antonio</p>
      <h1>Mobile Dental Anesthesiologist for Texas Practices</h1>
      <p class="hero-lede">
        General anesthesia in your office, delivered by Dr. Brett Harris &mdash; for pediatric,
        surgical, periodontal, implant, and general dentistry. One flat fee per case, no
        anesthesiologist on staff required.
      </p>
      <div class="hero-actions">
        <a href="#contact" class="btn btn-primary">Book Dr. Harris</a>
        <a href="#services" class="btn btn-ghost">See Services</a>
      </div>
    </div>
  </section>

  <section class="stats">
    <div class="wrap stats-grid">
      <div class="stat">
        <span class="stat-num">5+ Years</span>
        <span class="stat-label">Providing office-based dental anesthesia</span>
      </div>
      <div class="stat">
        <span class="stat-num">3-Year</span>
        <span class="stat-label">Hospital-based residency in dental anesthesiology</span>
      </div>
      <div class="stat">
        <span class="stat-num">Flat Fee</span>
        <span class="stat-label">Per case, billed to your practice</span>
      </div>
      <div class="stat">
        <span class="stat-num">TX Triangle</span>
        <span class="stat-label">Austin, San Antonio, Houston &amp; Dallas</span>
      </div>
    </div>
  </section>

  <section class="pull-quote">
    <div class="wrap">
      <blockquote>&ldquo;If I can&rsquo;t work with him, the case gets delayed.&rdquo;</blockquote>
      <p class="pull-quote-cite">Dr. Robert Friedberg, Board-Certified Periodontist &middot; Houston, TX</p>
    </div>
  </section>

  <section id="services" class="services">
    <div class="wrap">
      <p class="eyebrow center">Services</p>
      <h2 class="center">General Anesthesia for Every Kind of Dental Practice</h2>
      <p class="section-lede center">
        With the airway secured under general anesthesia, there&rsquo;s no patient movement
        and no airway to manage while you work &mdash; whatever the procedure. Dr. Harris
        supports:
      </p>

      <div class="service-grid">
{service_cards}
        <div class="service-card service-card-cta">
          <h3>Don&rsquo;t See Your Case Listed?</h3>
          <p>If the procedure can be done in a dental office, it can likely be done under general anesthesia. Reach out to discuss your case.</p>
          <a href="#contact" class="btn btn-ghost btn-small">Ask About Your Case</a>
        </div>
      </div>
    </div>
  </section>

  <section id="how-it-works" class="referring">
    <div class="wrap referring-inner">
      <p class="eyebrow">For Texas Dental Practices</p>
      <h2>Offer General Anesthesia in Your Office&mdash;No Anesthesiologist on Staff</h2>
      <p class="section-lede">
        If your practice has patients who need general anesthesia but no anesthesia coverage
        in-house, you&rsquo;re likely turning those cases away or sending them to a hospital.
        Dr. Harris comes to your office with everything needed, so your practice can keep them.
      </p>
      <div class="referring-points">
        <div class="referring-point">
          <h3>No In-House Anesthesia Team Needed</h3>
          <p>Dr. Harris and his equipment cover it entirely &mdash; nothing for your practice to hire, credential, or maintain.</p>
        </div>
        <div class="referring-point">
          <h3>Mobile, In-Office Service</h3>
          <p>We travel to your operatory anywhere in the Texas Triangle &mdash; Austin, San Antonio, Houston, and Dallas.</p>
        </div>
        <div class="referring-point">
          <h3>Flat, Predictable Per-Case Fee</h3>
          <p>One flat fee billed directly to your practice per case &mdash; no separate patient billing to manage.</p>
        </div>
      </div>

      <h3 class="how-heading">How It Works</h3>
{how_steps_html()}

      <div class="backup-callout">
        <h3>Already Have an Anesthesia Provider?</h3>
        <p>
          Many practices work with more than one. Keep Dr. Harris on call for the cases that
          need general anesthesia and for the days your usual provider is booked &mdash;
          including if you handle your own sedation today.
        </p>
      </div>
      <div class="hero-actions">
        <a href="#contact" class="btn btn-primary btn-on-dark">Book Dr. Harris</a>
        <a href="{RATE_SHEET}" class="btn btn-ghost btn-ghost-dark">Request Rate Sheet</a>
      </div>
    </div>
  </section>

  <section id="why" class="why">
    <div class="wrap">
      <p class="eyebrow center">Why a Dental Anesthesiologist</p>
      <h2 class="center">Not Every Anesthesia Provider Is Built for a Dental Office</h2>
      <p class="section-lede center">
        Medical anesthesiology groups and national scheduling agencies are moving into
        dentistry. Here&rsquo;s what&rsquo;s different when your anesthesia provider is a dentist.
      </p>
      <div class="why-grid">
        <div class="safety-item">
          <h3>Accountable to the Same Dental Board</h3>
          <p>Dr. Harris is a dentist, regulated by the same dental board you are. With a medical anesthesiology group, you and your anesthesia provider answer to different boards &mdash; so when it matters, you&rsquo;re not in it together.</p>
        </div>
        <div class="safety-item">
          <h3>Stays Until Discharge</h3>
          <p>Hospital anesthesiologists are used to handing patients off to recovery nurses. Dr. Harris monitors every patient through emergence and recovery, and stays until discharge criteria are met.</p>
        </div>
        <div class="safety-item">
          <h3>Knows How a Dental Office Runs</h3>
          <p>Trained as a dentist, he understands your operatory, your team, and where the real risks in office-based anesthesia are.</p>
        </div>
        <div class="safety-item">
          <h3>Dedicated Full-Time, Not a Side Gig</h3>
          <p>Mobile dental anesthesia is the whole of Dr. Harris&rsquo;s practice, with the equipment to match on every case.</p>
        </div>
        <div class="safety-item">
          <h3>Continuous Monitoring</h3>
          <p>Blood pressure, pulse oximetry, capnography, and cardiac monitoring maintained throughout every procedure.</p>
        </div>
        <div class="safety-item">
          <h3>Emergency Preparedness</h3>
          <p>Full emergency drug kit, advanced airway equipment, and resuscitation protocols on-site for every appointment.</p>
        </div>
      </div>
    </div>
  </section>

  <section id="testimonials" class="testimonials">
    <div class="wrap">
      <p class="eyebrow center">What Dentists Say</p>
      <h2 class="center">Trusted by Texas Surgeons and Dentists</h2>

      <div class="testimonial-grid">
{testimonial_figure("gonzalez")}

{testimonial_figure("chung")}

{testimonial_figure("friedberg")}
      </div>
    </div>
  </section>

  <section id="about" class="about">
    <div class="wrap about-grid">
      <div class="about-media">
        <div class="about-media-frame">
          <picture>
            <source srcset="/assets/dr-harris-headshot.webp" type="image/webp">
            <img src="/assets/dr-harris-headshot-crop.jpg" alt="Dr. Brett Harris, DMD" class="about-photo" width="880" height="1173" loading="lazy">
          </picture>
        </div>
        <p class="about-caption">Brett Harris, DMD &mdash; Founder, Harris Anesthesia Group</p>
      </div>
      <div class="about-copy">
        <p class="eyebrow">About the Practice</p>
        <h2>Dr. Brett Harris, DMD</h2>
        <p>
          Dr. Brett Harris completed a three-year, hospital-based residency in Advanced
          Education in Dental Anesthesiology at NYU Langone Hospitals before founding Harris
          Anesthesia Group to bring hospital-level anesthesia care into the dental office.
          Office-based anesthesia is all he does: Dr. Harris serves exclusively as the
          anesthesia provider, working alongside oral surgeons, periodontists, prosthodontists,
          general dentists, and pediatric dentists to keep patients safe, still, and comfortable.
        </p>
        <p>
          This model lets the treating dentist stay fully focused on the work while an
          independent, dedicated anesthesia provider manages airway, sedation depth,
          hemodynamics, and recovery &mdash; the same division of labor patients would expect in
          a hospital operating room, brought directly into your office.
        </p>
        <ul class="credential-list">
          <li>Doctor of Dental Medicine (DMD) &mdash; University of Nevada, Las Vegas School of Dental Medicine</li>
          <li>Advanced Education in Dental Anesthesiology &mdash; NYU Langone Hospitals (2017&ndash;2020)</li>
          <li>B.S., Management &mdash; Brigham Young University</li>
          <li>Focused exclusively on office-based dental anesthesia</li>
        </ul>
      </div>
    </div>
  </section>

  <section id="faq" class="faq">
    <div class="wrap faq-inner">
      <p class="eyebrow center">FAQ</p>
      <h2 class="center">Questions From Dental Practices</h2>
      <div class="faq-list">
{faq_html}
      </div>
    </div>
  </section>

  <section id="patients" class="patients">
    <div class="wrap patients-inner">
      <p class="eyebrow">For Patients</p>
      <h2>Having Anesthesia With Dr. Harris?</h2>
      <p>
        Dr. Harris provides anesthesia at your dentist&rsquo;s office as part of your treatment,
        so your appointment is scheduled through your dental office.
      </p>
      <ul class="credential-list">
        <li>Follow the instructions your dental office gives you before the appointment exactly, including when to stop eating and drinking.</li>
        <li>Plan for a responsible adult to take you home afterward.</li>
        <li>Dr. Harris stays with you through recovery until you&rsquo;re ready to go home.</li>
      </ul>
      <p class="patients-contact">Questions about your anesthesia? Call <a href="{PHONE_HREF}">{PHONE}</a>.</p>
    </div>
  </section>

  <section id="contact" class="contact">
    <div class="wrap contact-grid">
      <div class="contact-info">
        <p class="eyebrow">Get in Touch</p>
        <h2>Book Dr. Harris</h2>
        <p>
          Tell us about your practice and the cases you&rsquo;d like covered, and we&rsquo;ll get
          back to you to schedule. Prefer to see pricing first?
          <a href="{RATE_SHEET}">Request our rate sheet.</a>
        </p>
        <dl class="contact-details">
          <div>
            <dt>Phone</dt>
            <dd><a href="{PHONE_HREF}">{PHONE}</a></dd>
          </div>
          <div>
            <dt>Email</dt>
            <dd><a href="mailto:{EMAIL}">{EMAIL}</a></dd>
          </div>
          <div>
            <dt>Service Area</dt>
            <dd>The Texas Triangle &mdash; Austin, San Antonio, Houston &amp; Dallas</dd>
          </div>
        </dl>
      </div>
      <form class="contact-form" id="contact-form" action="https://formsubmit.co/{EMAIL}" method="POST">
        <input type="hidden" name="_subject" value="New inquiry from harrisanesthesia.com">
        <input type="hidden" name="_template" value="table">
        <input type="text" name="_honey" class="form-honeypot" tabindex="-1" autocomplete="off" aria-hidden="true">
        <div class="form-pair">
          <div class="form-row">
            <label for="name">Name</label>
            <input type="text" id="name" name="name" required>
          </div>
          <div class="form-row">
            <label for="role">I am a&hellip;</label>
            <select id="role" name="role">
              <option>Referring Doctor / Practice</option>
              <option>Patient</option>
              <option>Other</option>
            </select>
          </div>
        </div>
        <div class="form-pair">
          <div class="form-row">
            <label for="practice">Practice Name</label>
            <input type="text" id="practice" name="practice">
          </div>
          <div class="form-row">
            <label for="city">City</label>
            <select id="city" name="city">
              <option>Austin</option>
              <option>Houston</option>
              <option>Dallas</option>
              <option>San Antonio</option>
              <option>Other</option>
            </select>
          </div>
        </div>
        <div class="form-pair">
          <div class="form-row">
            <label for="practice-type">Practice Type</label>
            <select id="practice-type" name="practice_type">
              <option>Pediatric Dentistry</option>
              <option>Oral &amp; Maxillofacial Surgery</option>
              <option>Periodontics</option>
              <option>Prosthodontics / Implants</option>
              <option>General &amp; Cosmetic Dentistry</option>
              <option>Other</option>
            </select>
          </div>
          <div class="form-row">
            <label for="cases">Est. Cases per Month</label>
            <select id="cases" name="cases_per_month">
              <option>1&ndash;2</option>
              <option>3&ndash;5</option>
              <option>6&ndash;10</option>
              <option>10+</option>
              <option>Not sure</option>
            </select>
          </div>
        </div>
        <div class="form-pair">
          <div class="form-row">
            <label for="email">Email</label>
            <input type="email" id="email" name="email" required>
          </div>
          <div class="form-row">
            <label for="phone">Phone</label>
            <input type="tel" id="phone" name="phone">
          </div>
        </div>
        <div class="form-row">
          <label for="message">Message (optional)</label>
          <textarea id="message" name="message" rows="3"></textarea>
        </div>
        <button type="submit" class="btn btn-primary btn-block">Send Message</button>
        <p class="form-note" id="form-note" role="status"></p>
      </form>
    </div>
  </section>

</main>
""" + footer()

write("index.html", home)


# ------------------------------------------------------------- inner pages

def page(path, title, description, eyebrow, h1, lede, body_html, testimonial_key, related_heading, related_links):
    related = "\n".join(f'        <li><a href="/{slug}/">{name}</a></li>' for slug, name in related_links)
    html = head(title, description, path) + f"""
<main>

  <section class="hero page-hero">
    <div class="wrap hero-inner">
      <p class="eyebrow">{eyebrow}</p>
      <h1>{h1}</h1>
      <p class="hero-lede">{lede}</p>
      <div class="hero-actions">
        <a href="/#contact" class="btn btn-primary">Book Dr. Harris</a>
        <a href="{RATE_SHEET}" class="btn btn-ghost">Request Rate Sheet</a>
      </div>
    </div>
  </section>

  <section class="page-body">
    <div class="wrap prose">
{body_html}
      <h2>How It Works</h2>
{how_steps_html()}

      <h2>Why Practices Choose Dr. Harris</h2>
      <ul class="credential-list">
{chr(10).join(f'        <li>{p}</li>' for p in WHY_POINTS)}
      </ul>
    </div>
  </section>

  <section class="testimonials">
    <div class="wrap">
      <p class="eyebrow center">What Dentists Say</p>
      <div class="testimonial-single">
{testimonial_figure(testimonial_key)}
      </div>
    </div>
  </section>

  <section class="page-related">
    <div class="wrap">
      <h2>{related_heading}</h2>
      <ul class="link-list">
{related}
      </ul>
    </div>
  </section>

  <section class="cta-band">
    <div class="wrap">
      <h2>Ready to offer general anesthesia in your office?</h2>
      <div class="hero-actions">
        <a href="/#contact" class="btn btn-primary btn-on-dark">Book Dr. Harris</a>
        <a href="{PHONE_HREF}" class="btn btn-ghost btn-ghost-dark">Call {PHONE}</a>
      </div>
    </div>
  </section>

</main>
""" + footer()
    write(path.strip("/") + "/index.html", html)


def services_list_for_city():
    return "\n".join(
        f'        <li><a href="/{slug}/">{name}</a> &mdash; {service_card_text[slug]}</li>'
        for slug, name in SERVICES
    )


CITY_COPY = {
    "austin": (
        "chung",
        """      <h2>Office-Based Anesthesia for Austin Dental Practices</h2>
      <p>Austin practices regularly see patients who need general anesthesia &mdash; children who can&rsquo;t complete treatment awake, anxious adults, and long surgical cases. Without an anesthesia provider on staff, those cases get referred out or wait on a hospital schedule.</p>
      <p>Dr. Harris comes to your office in Austin and the surrounding communities, brings his own anesthesia, monitoring, and emergency equipment, and manages the case from the first dose until your patient meets discharge criteria.</p>""",
    ),
    "houston": (
        "friedberg",
        """      <h2>Office-Based Anesthesia for Houston Dental Practices</h2>
      <p>Houston practices that perform surgery under general anesthesia often depend on whichever anesthesia provider is available &mdash; and when that provider is booked, the case waits. Dr. Harris gives your office a dedicated dental anesthesiologist to call, whether as your primary provider or as your backup.</p>
      <p>He travels to practices in Houston and the surrounding communities with his own equipment, and stays with every patient through recovery until discharge criteria are met.</p>""",
    ),
    "dallas": (
        "chung",
        """      <h2>Office-Based Anesthesia for Dallas Dental Practices</h2>
      <p>Medical anesthesiology groups and national scheduling agencies are moving into dentistry. Dr. Harris is different: he&rsquo;s a dentist, accountable to the same dental board as your practice, and mobile dental anesthesia is his full-time work.</p>
      <p>He comes to practices in Dallas and the surrounding communities, so your patients can be treated under general anesthesia without leaving the office they already trust.</p>""",
    ),
    "san-antonio": (
        "gonzalez",
        """      <h2>Office-Based Anesthesia for San Antonio Dental Practices</h2>
      <p>Keep general anesthesia cases in your San Antonio office instead of referring them out. Dr. Harris brings everything needed for office-based general anesthesia &mdash; anesthesia, monitoring, and emergency equipment &mdash; to your operatory.</p>
      <p>Your practice pays one flat fee per case, with no anesthesia team to hire or credential, and Dr. Harris stays with every patient until discharge criteria are met.</p>""",
    ),
}

for slug, name in CITIES:
    tkey, intro = CITY_COPY[slug]
    body = intro + f"""

      <h2>Services for {name} Practices</h2>
      <ul class="credential-list">
{services_list_for_city()}
      </ul>
"""
    others = [(s, f"{n}, TX") for s, n in CITIES if s != slug]
    page(
        f"/{slug}/",
        f"Dental Anesthesiologist in {name}, TX | Harris Anesthesia",
        f"Mobile dental anesthesiologist Dr. Brett Harris brings general anesthesia to dental offices in {name}, TX. One flat fee per case.",
        f"{name}, Texas",
        f"Mobile Dental Anesthesiologist in {name}, TX",
        f"General anesthesia in your {name} office, delivered by a dedicated dental anesthesiologist &mdash; no anesthesiologist on staff required.",
        body,
        tkey,
        "Also Serving",
        others,
    )


FULL_ARCH_PROCEDURES = [
    ("All-on-X", "Full-arch implant-supported restoration requiring extended, motion-free anesthesia from first incision to final torque."),
    ("Zygomatic Implant Surgery", "Zygomatic implant placement in the severely atrophic maxilla, where precision and airway control are critical."),
    ("Pterygoid Implant Surgery", "Posterior maxillary implant placement engaging the pterygoid plates."),
    ("Full-Arch Placement with Sinus Lifts", "Combined implant and sinus augmentation procedures, managed with attention to airway positioning and case length."),
    ("Full-Mouth Extractions with Immediate Implants", "Same-day extraction and immediate implant placement in a single visit."),
    ("Alveoloplasty with Full-Arch Placement", "Bone recontouring combined with full-arch implant surgery."),
    ("Bone Block Grafting with Simultaneous Implants", "Hard-tissue grafting performed concurrently with implant placement."),
]

SERVICE_COPY = {
    "pediatric-dental-anesthesia": (
        "Pediatric Dental Anesthesia",
        "General anesthesia for children who need extensive dental treatment &mdash; in your own office, instead of waiting on hospital operating room time.",
        "chung",
        """      <h2>General Anesthesia for Children, in Your Own Office</h2>
      <p>Many young children can&rsquo;t sit through extensive treatment awake. General anesthesia lets your team complete the full treatment plan in a single visit, without sending the family to wait for hospital operating room time.</p>
      <p>Dr. Harris provides general anesthesia for pediatric patients in your office, monitors continuously throughout the procedure, and stays with the child through recovery until discharge criteria are met. Your team focuses on the dentistry.</p>""",
    ),
    "oral-surgery-anesthesia": (
        "Anesthesia for Oral &amp; Maxillofacial Surgery",
        "A dedicated anesthesia provider for your surgical cases, so the surgeon can stay fully focused on the surgical field.",
        "gonzalez",
        """      <h2>Anesthesia for Oral Surgery Practices</h2>
      <p>Oral surgery practices line up surgical cases for general anesthesia every week. With Dr. Harris managing anesthesia, the surgeon stays fully focused on the surgical field while a dedicated provider manages the airway, sedation depth, hemodynamics, and recovery.</p>
      <h2>Cases We Support</h2>
      <ul class="credential-list">
        <li>Extractions and third molars</li>
        <li>Bone grafting</li>
        <li>Dental implant placement</li>
        <li>Full-arch and advanced implant surgery</li>
      </ul>""",
    ),
    "periodontal-surgery-anesthesia": (
        "Anesthesia for Periodontal Surgery",
        "Periodontal and implant surgery performed under general anesthesia with a secured airway, in your office.",
        "friedberg",
        """      <h2>General Anesthesia for Periodontal Practices</h2>
      <p>Periodontal practices perform a lot of surgery. Under general anesthesia with a secured airway, there&rsquo;s no patient movement and no airway for your team to manage while you work, which matters most in long and technically demanding cases.</p>
      <p>Dr. Harris brings his own equipment, manages anesthesia from start to finish, and stays with your patient until discharge criteria are met.</p>""",
    ),
    "full-arch-implant-anesthesia": (
        "Anesthesia for Full-Arch &amp; Advanced Implant Surgery",
        "Extended, motion-free general anesthesia for All-on-X and complex implant cases, in your own office.",
        "gonzalez",
        """      <h2>Anesthesia for Long, Complex Implant Cases</h2>
      <p>Full-arch cases are long, and they demand a still patient and a secure airway from the first incision to the final torque. Dr. Harris manages anesthesia for the entire case so your surgical team can focus on the restoration.</p>
      <h2>Procedures We Support</h2>
      <ul class="credential-list">
""" + "\n".join(f"        <li><strong>{n}</strong> &mdash; {d}</li>" for n, d in FULL_ARCH_PROCEDURES) + """
      </ul>""",
    ),
    "general-cosmetic-dental-anesthesia": (
        "Anesthesia for General &amp; Cosmetic Dentistry",
        "Complete extensive restorative and cosmetic treatment plans in a single visit under general anesthesia, in your own office.",
        "chung",
        """      <h2>Anesthesia for General and Cosmetic Practices</h2>
      <p>Extensive restorative and cosmetic treatment plans, and anxious patients who avoid the dentist, can often be completed in a single visit under general anesthesia &mdash; without referring the patient elsewhere.</p>
      <p>Dr. Harris comes to your office with his own equipment, so your practice can offer general anesthesia without hiring or credentialing an anesthesia team.</p>""",
    ),
}

SERVICE_SEO = {
    "pediatric-dental-anesthesia": ("Pediatric Dental Anesthesia in Texas", "General anesthesia for pediatric dental patients, in your own office."),
    "oral-surgery-anesthesia": ("Oral Surgery Anesthesia in Texas", "General anesthesia for oral surgery cases, in your own office."),
    "periodontal-surgery-anesthesia": ("Periodontal Surgery Anesthesia in Texas", "General anesthesia for periodontal and implant surgery, in your own office."),
    "full-arch-implant-anesthesia": ("Full-Arch Implant Anesthesia in Texas", "General anesthesia for All-on-X and complex implant surgery, in your own office."),
    "general-cosmetic-dental-anesthesia": ("Dental Anesthesia for General Dentists in Texas", "General anesthesia for restorative and cosmetic treatment, in your own office."),
}

city_links = [(s, f"{n}, TX") for s, n in CITIES]
for slug, name in SERVICES:
    h1, lede, tkey, body = SERVICE_COPY[slug]
    seo_title, seo_lead = SERVICE_SEO[slug]
    page(
        f"/{slug}/",
        f"{seo_title} | Harris Anesthesia",
        f"{seo_lead} Serving Austin, Houston, Dallas &amp; San Antonio. One flat fee per case.",
        "Services",
        h1,
        lede,
        body,
        tkey,
        "Available Across the Texas Triangle",
        city_links,
    )


# ---------------------------------------------------------------- sitemap

urls = ["/"] + [f"/{s}/" for s, _ in CITIES] + [f"/{s}/" for s, _ in SERVICES]
sitemap = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
sitemap += "".join(f"  <url>\n    <loc>{SITE}{u}</loc>\n  </url>\n" for u in urls)
sitemap += "</urlset>\n"
with open(os.path.join(ROOT, "sitemap.xml"), "w", encoding="utf-8", newline="\n") as f:
    f.write(sitemap)

print("built", len(urls), "pages")
