import streamlit as st
import streamlit_authenticator as stauth
import firebase_admin
from firebase_admin import firestore
from firebase_admin import credentials
from firebase_admin import auth
import pandas as pd
from streamlit_tags import st_tags, st_tags_sidebar
a= ['appel', 'concours', 'prix', 'design', 'awards', 'candidatures', 'photographie', 'international', 'saison', 'fourniture', 'acquisition', 'dart'
    , 'conception', 'participation','jury', 'système','services', 'art', 'matériels', 'doffres', 'mise', 'call', 'achat', 'informatiques', 
    'installation', 'digital', 'informatique', 'avis', 'livraison', 'hospitality', 'london', 'iluxury', 'matériel', 'scenic', 'vistas', 
    'magazine', 'gravure', 'mario', 'avati', 'furniture', 'fit', 'sit', 'inspirations', 'marché', 'pratic', 'pergola', 'evolution', 'nature', 
    'bormioli', 'pharma', 'redraw', 'capsule', 'nakagin', 'produits', 'blt', 'built','lighting', 'chelsea', 'bains', 'thermaux', 'lhimalaya',
   'objet', 'projets', 'thème', 'limage', 'exposition', 'photographies', 'dautoportraits', 'perdu', 'trouvé','marque','master', 'darchitecture',
  'salon', 'talents', 'artistiques', 'padoue', 'européens', 'artistes', 'sportif', 'troisième', 'édition', 'reconnaissance','canapé', 
  'modulaire', 'dextérieur', 'pôle', 'déconomie', 'circulaire', 'couleurs', 'vibrantes', 'lhospitalité', 'distanbul', 'bouchons', 'tour',
 '5e', 'maintenance', 'photography', 'entries', 'competition', 'dune', 'bureau', 'équipements', 'consommables', 'service', 'fournitures',
 'recrutement', 'season', 'constitution', 'itissalat', 'demande', 'dappel', 'maghrib', 'développement', 'consultant', 'formation', 
 'déquipements', 'manifestation', 'linstallation', 'réseau', 'programme', 'recherche', 'dintérêt', 'cadre', 'projet', 'place', 'talent', 'gestion',
'ppm', 'tic', 'travaux', 'nomination', 'référence', 'fournisseurs', 'internet', 'profit', 'données', 'conseil', 'prestataire', 'réparation',
'equipements','base', 'termes', 'entry', 'logiciel', 'solution', 'renouvellement', 'cabinet', 'lance', 'juried', 'communications', 'renforcement',
'biopama', 'entretien', 'prestataires', 'startups', 'decoles', 'répertoire', 'supply', 'assistance', 'licences', 'fournir', 'offre', 'systeme',
'consultation', 'lot', 'national', 'accessoires', 'dordinateurs', 'lacquisition', 'aaoi', 'pièces', 'vue', 'portables', 'œuvre', 'niveau', 
'financement', 'technique', 'lambassade', 'séminaire', 'médias', 'materiel', 'system', 'imprimantes', 'sélection', 'plateforme', 'systèmes', 
'dinformation', 'daccessoires', 'numérique', 'divers', 'étatsunis', 'déclaration', 'himalayan', 'thermal', 'baths', 'themeless', 'captured',
'self', 'portrait', 'exhibition', 'lost', 'found', 'brand','architecture', 'masterprize', 'fair', 'padua', 'european', 'artists', 'académie',
'compte', 'fournisseur', 'communication', 'doffre', 'support', 'entreprises', 'prestation', 'location', 'logiciels', 'equipement', 'techniques',
'web', 'lactualisation', 'kits', 'surveillance', 'initiative', 'deux', 'eoi', 'sécurité', 'guinée', 'centres', 'direction', 'sport', 'third', 
'edition', 'sea', 'cash','outdoor', 'modular', 'market', 'circular', 'economy', 'hub', 'projects', 'vibrant', 'colors', 'contest', 'istanbul', 
'china', 'hardware', 'products', 'tower', 'cap', 'recognition','digitalisation', 'spécialiste', 'devis', 'site', 'solutions', 'serveurs', 
'déquipement', 'petites', 'machines', 'réalisation','pose', 'consommable', 'réseaux', 'expert', 'appui', 'ouvert', 'connexion', 'photocopieurs', 
'consultants', 'lannée', 'étude', 'additif', 'salle', 'mobilier', 'multinational', 'individuel', 'concevoir', 'passation','construction',
'conférence', 'provision', 'developpement', 'request', 'plan', 'tablettes', 'câbles', 'proposition', 'nouvelle', 'contrat', 'assurer', 
'propositions', 'linfrastructure', 'panel', 'moyennes', 'materiels', 'transport', 'realisation', 'bureaux', 'santé', 'partenariat', 'annuelle',
'donnees', 'contrôle', 'fournisseursprestataires', 'relative', 'simplifié', 'téléphonie', 'congo', 'marchés','auditorium', 'numériques', 'mobile',
'évaluation', 'audiovisuels', 'development', 'consultancy', 'equipment', 'office', 'food', 'préqualification', 'développer', 'stratégique',
'province', 'licence', 'compris', 'doutils', 'évaluer', 'rfp', 'gouvernance', 'imprimante', 'caméra', 'responsable', 'électrique', 'ndici',
'mobiles', 'soutien', 'stockage', 'câblage', 'fibre', 'dupw', 'conclusion', 'dinfrastructures', 'long', 'terme', 'distribution', 'contre',
'diagnostics', 'mpme', 'ordinateurs', 'centre', 'relatif', 'dentretien', 'etude', 'publication', 'parc', 'capacité', 'caméras', 'planification', 
'ambassade', 'visioconférence', 'local', 'portant', 'report', 'multifonctions', 'radio', 'charge', 'détudes', 'securite', 'infrastructure', 
'lots', 'parsebalt', 'coigpsaac2023004', 'nouveau', 'connectivité', 'senior', 'nationaux', 'lutte', 'lextension', 'dapprovisionnement'
, 'sms', 'pepfar', 'programmes', 'aps', 'agpm', 'paiements', 'communautaires', 'papeterie', 'vidéographie', 'africain', 'faculté', 'sciences',
'accompagnement', 'progiciel', 'uganda', 'technical', 'rwanda', 'vendor', 'prequalification', 'rfid', 'hiring', 'production', 'annuel', 'embauche',
'sénégal', 'portail', 'télécommunication', 'vidéosurveillance', 'processus','prorogation', 'regionale', 'logicielles', 'dévaluation', 
'dalimentation', 'clé', 'hp', 'livrer', 'invitation', 'soumettre', 'lévaluation', 'lexamen', 'multimédia', 'toners', 'soumission', 'audit',
'moyenne', 'gérés', 'dentrepreneurs', 'bâtiment', 'installer', 'potentiels', 'dinfrastructure', 'montage', 'stations', 'projecteur', 'suivi',
'vidéo', 'rft', 'cotation', 'trois', 'numérisation', 'migration', 'dp', 'offres', 'confection', 'raccordement', 'daménagement', 'intrusion',
'équipement', 'onduleurs', 'intelligents', 'réhabilitation', 'camera', 'commande', 'damenagement', 'espace', 'souk', 'lupw', 'rechange',
'protection', 'pc', 'promotion', 'promouvoir', 'rectificatif', 'acquérir', 'intégrée', 'comptabilité', 'unique', 'mairie', 'mécanisme',
'électronique', 'bureautiques', 'qualité', 'périinformatiques', 'vingt', 'dinstallation', 'détection', 'multimédias', 'configuration', 
'intégration', 'hr', 'umwuga','dappui', 'reunion', 'section', 'diplomatie', 'kit', 'date', 'deploiement', 'cotations', 'linstitut', 'lapplication', 
'reseau', 'droits', 'etudes', 'cameroun', 'banque', 'dossier', 'études', 'opérateurs', 'société', 'evaluation', 'ethio', 'telecom', 'invite', 
'tous', 'soumissionnaires', 'faisabilité', 'optique', 'eau', 'gabon', 'poste', 'bande', 'dimprimantes', 'terrain', 'equatoriale', 'publicité',
'publicitaires', 'addendum', 'générale', 'audiovisuel', 'vrac', 'renseignements', 'locaux', 'ligne', 'center', 'conference', 'fonds', 'démocratie',
'régionale', 'besoin', 'destiné', 'ladministration', 'compensation', 'dautomatisation', 'lobservation', 'delivery','embassy', 'annual', 'hacp',
'intérêt', 'enquêteur', 'investigations', 'niger','proposal', 'investment', 'information', 'work', 'financial', 'health', 'abridged', 'bid',
'notice', 'epson', 'govnet', 'chauffeur', 'retainer', 'réservé', 'uniquement', 'auto', 'constituer', 'initiatives', 'sonorisation', 'terre',
'finale', 'hpbha', 'attributions', 'provisoires', 'technologie', 'dordonnancement', 'firme', 'exploitation', 'rdc', 'inclure', 'vulnérables', 
'action', 'bars', 'ktrn', 'rcs', 'fawe', 'videography', 'scanners', 'hungry', 'accessories', 'develop', 'cyber', 'software', 'network', 
'security', 'firm', 'dinvestissement', 'abrégé', 'ouganda', 'lexploitation', 'lécole', 'puces', 'agricole', 'diffusion', 'laboratoire', 
'pilotage', 'renforcer', 'gsm', 'soudan', 'circuit', 'systemes', 'choix', 'établissements', 'dexigences', 'courtage', 'lapiculture', 
'oneebrancheeau', 'physique', 'electronique', 'archives', 'despace', 'média', 'besoins', 'firewalls', 'lecole', 'capture', 'dinterprétation',
'opérationnelles', 'commune', 'quartier', 'mkhalif', 'sbaa', 'desktops', 'laptops', 'thermographique', 'berrechid', 'lagence', 'secrétariat',
'relation', 'client', 'lapprovisionnement', 'finances', 'mitel', 'mois', 'profondeur', 'danesthésie', 'tbh', 'placement', 'dix', 'approprié', 
'lspid', 'sonicwall', 'dell', 'jeux', 'barres', 'tubulaires', 'ferme', 'lecteur', 'pinces', 'fixation', 'lélaboration', 'politiques', 'léquipement',
'réparations', 'serrecâbles', 'conformément', 'spécifications', 'détiquette', 'icasa', 'annulation', 'lappel', 'réputé', 'cette', 'prévoit',
'belden', 'câble', 'faible', 'bruit', 'conditions', 'dimpression', 'relations', 'publiques', 'vérification', 'juridique', 'world', 'travel', 'nob',
'esaro', 'daudit', 'effectuer', 'dappareillage', 'tension', 'secours', 'interventions', 'defficacité', 'énergétique', 'nieuwoudtville', 'brandvlei',
'nersa', 'infonuagiques', 'publics', 'joints', 'période', 'ans', 'réannonce', 'disposition', 'actualisation', 'configurer', 'clôture', 'haute',
'manuel', 'isolateur', 'aides', 'formelle', 'dt', 'facilité', 'coopération', 'denquêteurs', 'pièges', 'audiovisuelle', 'sap', 'acoustique', 
'sousmarin', 'relevage','microphones', 'groupe', 'transfert', 'compétences', 'spécialistes', 'régulateur', 'reannonce', 'pa', 'dossiers', 'laser',
'associés', 'backline', 'imscloud', 'repartie', 'cadres', 'métalliques', 'chambres', 'final', 'clients', 'complexe', 'téléphonique', 'miliana',
'anti', 'tipaza', 'télésurveillance', 'siège', 'affranchissement', 'billetterie', 'dot', 'alger', 'contrats', 'dadhésions', 'commandes',
'manutention', 'lexmark', 'barrière', 'levante', 'algérie', 'startup', 'daccueil', 'accessoire', 'assainissement', 'fibres', 'optiques',
'canalisation', 'déplacement', 'pièce', 'passifs', 'foudre','gab', 'ncr', 'cemb', 'temouchent', 'acquisitions', 'onefd', 'paires', 'connecteurs',
'présente', 'liberté', 'presse', 'angola', 'préparer', 'prochaine', 'génération', 'leaders', 'seme','concernant', 'première', 'vague', 
'apiculteurs', 'maep', 'moyens','dinnovation', 'cuisson', 'scc', 'dingénierie', 'intranet', 'douvrages', 'spécialisés', 'lunstim', 
'redynamisation', 'paramétrage','affaiblissement', 'amélioration', 'parcours', 'académique', 'débit', 'aao', 'bénin', 'enregistreurs', 'appareils',
'magasin', 'communes', 'tenue', 'guichet', 'communautaire', 'motos', 'valeurs', 'inactifs', 'rideaux', 'salles', 'elaborer', 'mode', 'pérennisation'
, 'ddaep', 'matière', 'abonnement', 'consommation', 'dsa', 'encres', 'téléphoniques', 'maladho', 'barry', 'convention', 'filière', 
'contractualisation', 'access', 'agriculture', 'padmar', 'individuels', 'courriers', 'version', 'tom', 'appels', 'avenant', 'gaborone',
'botswana', 'pd', 'traitement', 'lanptic', 'smartphone','rentrée', 'dpeps', 'blk', 'bumigeb','repertoire', 'carfo', 'matérielles', 'trésor',
'structures', 'didactiques', 'cellules', 'bobine', 'point', 'scada', 'quarantesix', 'partenaires', 'dexécution', 'informatiques66', 'desktop',
'pluralisme', 'contribuer','interet', 'dinteret', 'bujumbura', 'burundi', 'dinterconnexion', 'bad', 'biennale', 'interneta', 'cellule', 'drône',
'achats', 'neufs', 'sonara','lerp', 'selection', 'laudit','mètres', 'hauteur', 'six', 'largeur', 'maitrise', 'dœuvre', 'linformatisation',
'parking', 'geoportail', 'radiocommunication', 'societe', 'aeroports', 'incendie', 'procédure', 'durgence', 'nangaeboko', 'dequipement',
'oracle', 'jour', 'capacites', 'lhyper', 'convergence', 'communaute', 'urbaine', 'lequipement', 'élaboration', 'schéma', 'directeur', 'ministère',
'dappoint', 'solaire', 'revision', 'serveur', 'preselection', 'droit', 'camerounais', 'teleprompteurs', 'autocue', 'msp20', 'feicom', 'titre', 
'independants', 'ecrans', 'teleaffichage', 'laeroport', 'lunite', 'video', 'pris','juin', 'bonne', 'domaines', 'hydrologique', 'hydraulique', 
'archimaintenant', 'accélération', 'transformation', 'mondialeobjet', 'general', 'mobiliers', 'chri', 'studio', 'cellulaire', 'civile', 
'contribution', 'api', 'délégataire', 'public', 'dorsale', 'intégré', 'giz', 'côte', 'ivoire', 'sbc', 'multifournisseurs', 'développeur', 
'tcis', 'f257', 'progres', 'defis', 'refonte', 'sanitaire', 'rca', 'tunisienne', 'standard', 'adolescents', 'turquie', 'rétroaction', 'découte',
'nationale', 'dassuit', 'statisticien', 'loutil', 'dassainissement', 'innovantes', 'léducation', 'addisabeba', 'dinformations','pratiques',
'luneca', 'spn', 'éthiopie', 'gérer', 'lunité', 'regulatory', 'sandbox', 'reference', 'fonctionnalite', 'maison', 'nations', 
'table', 'st', 'pupitres', 'doubles', 'manioc', 'étages', 'code', 'court', 'masse', 'cahiers', 'radar', 'barrières', 
'tarifaires', 'radars', 'éducation', 'accroître', 'consolidation', 'dappareils', 'gikace', 'creationoperationnalisation', 'conseillerère',
'enseignants', 'elèves', 'secondaire', 'placesystème','ambassadeur','analyse', 'détaillée', 'collecte', 'équatoriale', 'automatisé', 'régionaux',
'télévisés', 'dagence', 'télévision', 'restreint', 'labonnement', 'outil', 'healthconnekt', 'engagement', 'pays', 'sauvegarde', 'shure',
'accordcadre', 'dinstallations', 'multifonctionnelles', 'daccessibilité', 'microsoft', 'rapport', 'danalyse', 'déléments', 'mécaniques',
'ups', 'dhébergement','alimentation', 'électricité', 'électroniques','gadgetssystème', 'reparation', 'chef', 'déquipe', 'autonomisation',
'entreprendre', 'lanalyse', 'exigences', 'letablissement', 'réaménagement','permettre', 'femmes', 'sadapter', 'changement', 'climatique', 
'innovations', 'steam', 'ideathon', 'établissement', 'restauration', 'lta', 'imprimantesphotocopieur', 'pvsystem', 'inkl', 'battery', 'storage',
'backupgenerator', 'gouvernementaux', 'présentation', 'écran', 'callcenter', 'supports', 'visibilité', 'ecran', 'projection', 'motorisé', 
'tensionné','republication', 'agence', 'mémo','madagascar', 'accord', 'portails', 'dampoules', 'diodes', 'électroluminescentes', 'lenvironnement', 
'adl', 'annonce', 'nrb', 'denseignement', 'langlais', 'lamerican', 'readvertized', 'prend', 'communicationback', 'school', 'mali', 'usaidmali', 
'shifin','guide', 'draglines','ios', 'dantivirus', 'destine', 'secretariat', 'caisse', 'main', 'global', 'fax', 'telephones', 'météorologique',
'marrakech', 'photographiques', 'diverses', 'dispositif', 'centraux', 'parcs', 'remise', 'état', 'éléments', 'installations', 'projecteurs', 
'led', 'small', 'medium', 'oneweek', 'windhoek', 'survey', 'install', 'detection', 'systems', 'travelling', 'administration', 'associate',
'review','improve', 'economic', 'activities', 'nigeria', 'creative', 'observatory', 'procurement', 'supplies', 'applications', 'expression', 
'interest', 'bank', 'payments', 'community', 'grants', 'combat', 'democracy', 'human', 'rights', 'accountability', 'acceleration', 'project',
'cellphone', 'bangui', 'candidates', 'ambassadorrsquos', 'special', 'selfhelp', 'fund', 'reduce', 'respond', 'trafficking', 'hotels', 'restaurents',
'quotation', 'servers', 'proposals', 'upgrade', 'situation', 'customer', 'relationship', 'materials', 'training', 'printer', 'purchase', 
'microchips', 'risk', 'assessment', 'farm', 'management', 'application', 'company', 'provide', 'customize', 'bulk', 'capacity', 'smart', 
'procuring', 'tools', 'roll', 'paperless', 'land', 'media', 'provisionaudiovisual', 'content', 'registration', 'strategic', 'external', 
'referral', 'hospital', 'assess', 'readiness', 'consulting', 'examinez', 'installez', 'dintrusion', 'dopérateurs', 'haut', 'réf', 'catégorie',
'catégories', 'engager', 'dagences', 'adjoint', 'principal','améliorer', 'activités', 'économiques', 'nigéria', 'dobservation', 'candidature',
'dexpression', 'commutateur', 'subventions', 'lutter', 'lhomme', 'responsabilité', 'daccélération', 'candidatses', 'spécial', 'dautoassistance', 
'lambassadeur', 'réduire', 'répondre', 'traite', 'conférences', 'hôtels', 'restaurants', 'financières', 'matériaux', 'lauditorium', 'leurs',
'cyberrisques', 'offrir', 'travailler', 'réseauter', 'entreprise', 'cybersécurité', 'états', 'déployer', 'cadastre', 'denregistrement', 'externe',
'préparation', 'accompagner', 'loptimisation', 'campus','utiliser', 'vpn', 'sites', 'smss', 'infrastructures', 'modèles', 'microcrédit', 'san', 
'sig', 'publié', 'rlf', 'fda', 'jeunesse', 'modèle', 'soustraitance', 'door', 'dakar','organisation', 'réunion', 'wcar', 'developper', 'entente',
'soumissions', 'lanacim', 'déploiement', 'lintégration','autocommutateur', 'onpremise','fixes', 'travers', 'innovant', 'daccès', 'technologies',
'bourses', 'marines', 'msp', 'dict', 'périphériques', 'arabophone', 'seychelles', 'impression', 'documents', 'soins', 'néonatals',
'slsb', 'dimprimantescopieurs', 'délégation', 'personnel', 'john', 'lewis', 'minority', 'fellows', 'approches', 'menées', 'localement',
'welthungerhilfe', 'isp', 'provider', 'opérationnaliser', 'opérations', 'loms', 'programmation', 'zone', 'dattente', 'transports', 'mbabane',
'chargé', 'instruments', 'financiers', 'microassurance','institutionelle', 'beratung', 'der', 'miparcours', 'enseignement', 'tchad', 'scanner',
'combler', 'vide', 'éducatif', 'tirer', 'parti', 'soutenir', 'stratégie', 'jeunes', 'résilience', 'face', 'lextrémisme', 'togo', 'pravost', 'sage',
'vers', 'frp', 'core', 'papier', 'copieurs', 'procédures', 'modelisation', 'partie', 'blocs', 'elaboration', 'politique', 'pointage', 
'mpls', 'lot2', 'topographique', 'oeuvre', 'imprimés', 'papiers', 'lhôpital', 'universitaire', 'aménagement', 'dequipements', 'decharges', 
'controlees', 'openlab', 'materiaux', 'delectrecite', 'scolaires', 'opérateur', 'postes', 'radios', 'portatifs', 'via', 'réactifs', 'eléments',
'rayonnage', 'modulaires', 'dacquisition', 'marche', 'connectiques', 'batteries', 'condensateurs', 'ip', 'itb', 'goods', 'lumière', 'tv', 
'décrans', 'interactifs', 'amlcft', 'lavushimanda', 'lutilisation', 'potentielle', 'science', 'consultance', 'tonner', 'hôtes', 'taille', 
'régime', 'médical', 'géré', 'dentreprise','gym', 'laboratoires', 'hospitaliers', 'readvert', 'zimbabwe', 'maghreb', 'tissalat', 'almaghrib']

cred = credentials.Certificate("projectflexgroup-6f2283fa5ba9.json")

if not firebase_admin._apps:
    firebase_admin.initialize_app(cred)

def set_query_params(signedin):
    query_params = {"signedin": signedin}
    st.experimental_set_query_params(**query_params)

def app():
    st.title('Bienvenue à Offrematch')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''

    def f():
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email

            global Usernm
            Usernm = (user.uid)

            st.session_state.signedout = True
            st.session_state.signout = True

            # Set the query parameter "signedin" to True for redirection
            set_query_params(True)

        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.signedout = False
        st.session_state.username = ''

    if "signedout" not in st.session_state:
        st.session_state["signedout"] = False
    if 'signout' not in st.session_state:
        st.session_state['signout'] = False

    if not st.session_state["signedout"]:
        choice = st.selectbox('Login/Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')

        if choice == 'Sign up':
            username = st.text_input("Enter  your unique username")

            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)

                st.success('Account created successfully!')
                st.markdown('Please Login using your email and password')
        else:
            st.button('Login', on_click=f)

    if st.session_state.signout:
        st.text('Name ' + st.session_state.username)
        st.text('Email id: ' + st.session_state.useremail)
        st.button('Sign out', on_click=t)

def display_data_page():
    # Check if the query parameter "signedin" is present and True
    if st.experimental_get_query_params().get("signedin", False):
        # Exemple de dataset avec trois colonnes : "Nom", "Age" et "Score"
        #dataset1 = pd.read_excel("C:\\Users\\HP\\Desktop\\projet_flex\\data_final66_70.xlsx")
        #dataset2 = pd.read_excel("C:\\Users\\HP\\Desktop\\projet_flex\\data_final.xlsx")
        dataset1 = pd.read_excel("data_final66_70.xlsx")
        dataset2 = pd.read_excel("data_final.xlsx")
 
        # Afficher une zone de texte pour l'entrée utilisateur
        #user_input = st.text_input('Entrez vos mots-clés séparés par des espaces', '')
        keywords = st_tags(
                            label='# Saisissez des mots-clés :',
                            text='Appuyez sur Entrée pour ajouter plus',
                            suggestions=a,
                            maxtags=10,
                            key="aljnf")
        # Afficher un bouton pour soumettre le texte
        if st.button('Soumettre'):
            # Convert the user input into a list of keywords
            
            filtered_dataset = pd.DataFrame(columns=dataset2.columns)
            print(keywords)
            for keyword in keywords:
                condition = dataset2['Title'].str.contains(keyword, case=False, na=False)
                filtered_rows = dataset2[condition]
                filtered_dataset = pd.concat([filtered_dataset, filtered_rows])
            #filtered_dataset = dataset2[filter_condition]
            # Check if the filtered dataset is not empty before displaying it
            if not filtered_dataset.empty:
                # Afficher les données filtrées sous forme de blocs avec un meilleur design
                st.write("## Appels d'offres")
                for idx, row in filtered_dataset.iterrows():
                    st.write(f"### {row['Title']}")
                    st.write(f"**Pays**: {row['Pays']}")
                    st.write(f"**Date limite**: {row['Date limite']}")

                    # Insérer un lien cliquable dans le bloc
                    url = row['Lien']
                    st.markdown(f"**Lien**: [{url}]({url})")

                    # Ajouter une séparation entre les blocs
                    st.divider()
            else:
                st.warning("Aucune donnée ne correspond à votre recherche.")
        else:
            # Afficher les données sous forme de blocs avec un meilleur design
            st.write("## Appels d'offres du jour")

            for idx, row in enumerate(dataset1["Title"]):
                st.write(f"### {row}")
                st.write(f"**Pays**: {dataset1['Pays'][idx]}")
                st.write(f"**Date limite**: {dataset1['Date limite'][idx]}")

                # Insérer un lien cliquable dans le bloc
                url = dataset1['Lien'][idx]
                st.markdown(f"**Lien**: [{url}]({url})")

                # Ajouter une séparation entre les blocs
                st.divider()

    else:
        # If the user is not logged in, display the login page
        app()

if __name__ == '__main__':
    # Check if the query parameter "signedin" is present and True
    if st.experimental_get_query_params().get("signedin", False):
        # If the user is logged in, display the data page
        display_data_page()
    else:
        # If the user is not logged in, display the login page
        app()
        
# Copyright © 2023 Latifa Benidder FLEX group. All rights reserved.
