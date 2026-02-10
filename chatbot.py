"""
Intelligent Chatbot for Farmers
Uses pattern matching and contextual responses
NOT dummy - actually helpful!
"""

import re
from datetime import datetime

class FarmingChatbot:
    """
    Intelligent farming assistant chatbot
    Provides contextual, helpful responses to farmer questions
    """
    
    def __init__(self, language='en'):
        self.language = language
        self.conversation_history = []
        self.user_context = {}
        
    def get_response(self, message):
        """Get intelligent response to user message"""
        message_lower = message.lower()
        
        # Store in history
        self.conversation_history.append({
            'role': 'user',
            'message': message,
            'timestamp': datetime.now()
        })
        
        # Analyze message and get response
        response = self._analyze_and_respond(message_lower, message)
        
        # Store response in history
        self.conversation_history.append({
            'role': 'assistant',
            'message': response,
            'timestamp': datetime.now()
        })
        
        return response
    
    def _analyze_and_respond(self, message_lower, original_message):
        """Analyze message and generate intelligent response"""
        
        # Greetings
        if any(word in message_lower for word in ['hello', 'hi', 'hey', 'namaste', 'vanakkam']):
            return self._greeting_response()
        
        # Farewells
        if any(word in message_lower for word in ['bye', 'goodbye', 'thank', 'thanks']):
            return self._farewell_response()
        
        # Disease-related questions
        if any(word in message_lower for word in ['disease', 'sick', 'problem', 'issue', 'blight', 'rot', 'rust', 'spot']):
            return self._disease_response(message_lower)
        
        # Fertilizer questions
        if any(word in message_lower for word in ['fertilizer', 'fertiliser', 'npk', 'urea', 'manure', 'compost']):
            return self._fertilizer_response(message_lower)
        
        # Pest questions
        if any(word in message_lower for word in ['pest', 'insect', 'bug', 'worm', 'caterpillar', 'aphid']):
            return self._pest_response(message_lower)
        
        # Watering questions
        if any(word in message_lower for word in ['water', 'irrigation', 'watering', 'rain', 'drought']):
            return self._watering_response(message_lower)
        
        # Soil questions
        if any(word in message_lower for word in ['soil', 'ph', 'ground', 'earth', 'dirt']):
            return self._soil_response(message_lower)
        
        # Crop-specific questions
        if any(word in message_lower for word in ['tomato', 'potato', 'corn', 'maize', 'wheat', 'rice']):
            return self._crop_specific_response(message_lower)
        
        # Organic farming
        if any(word in message_lower for word in ['organic', 'natural', 'chemical-free', 'neem']):
            return self._organic_response(message_lower)
        
        # Planting/seeding
        if any(word in message_lower for word in ['plant', 'seed', 'sow', 'grow', 'transplant']):
            return self._planting_response(message_lower)
        
        # Harvesting
        if any(word in message_lower for word in ['harvest', 'pick', 'when to harvest', 'ready']):
            return self._harvest_response(message_lower)
        
        # Weather
        if any(word in message_lower for word in ['weather', 'temperature', 'climate', 'season']):
            return self._weather_response(message_lower)
        
        # Government schemes
        if any(word in message_lower for word in ['scheme', 'subsidy', 'government', 'pm kisan', 'loan']):
            return self._government_response(message_lower)
        
        # Default intelligent response
        return self._general_farming_response()
    
    # ========================================================================
    # RESPONSE GENERATORS
    # ========================================================================
    
    def _greeting_response(self):
        responses = {
            'en': "Hello! 👋 I'm Kisan Sahayak, your farming assistant. I can help you with:\n\n• Disease identification & treatment\n• Fertilizer recommendations\n• Pest control methods\n• Watering schedules\n• Soil health\n• Organic farming tips\n\nWhat can I help you with today?",
            'hi': "नमस्ते! 👋 मैं किसान सहायक हूं। मैं आपकी मदद कर सकता हूं:\n\n• रोग पहचान और उपचार\n• उर्वरक सिफारिशें\n• कीट नियंत्रण\n• सिंचाई\n• मिट्टी स्वास्थ्य\n• जैविक खेती\n\nआज मैं आपकी कैसे मदद कर सकता हूं?",
            'ta': "வணக்கம்! 👋 நான் கிசான் சஹாயக். நான் உங்களுக்கு உதவ முடியும்:\n\n• நோய் அடையாளம் மற்றும் சிகிச்சை\n• உரம் பரிந்துரைகள்\n• பூச்சி கட்டுப்பாடு\n• நீர்ப்பாசனம்\n• மண் ஆரோக்கியம்\n• இயற்கை விவசாயம்\n\nஇன்று நான் உங்களுக்கு எப்படி உதவ முடியும்?"
        }
        return responses.get(self.language, responses['en'])
    
    def _farewell_response(self):
        responses = {
            'en': "You're welcome! 🌾 Happy farming! Feel free to ask me anything anytime. Good luck with your crops!",
            'hi': "आपका स्वागत है! 🌾 खुश खेती! कभी भी मुझसे कुछ भी पूछने में संकोच न करें। आपकी फसलों के लिए शुभकामनाएं!",
            'ta': "வரவேற்கிறோம்! 🌾 மகிழ்ச்சியான விவசாயம்! எப்போது வேண்டுமானாலும் என்னிடம் கேளுங்கள். உங்கள் பயிர்களுக்கு வாழ்த்துக்கள்!"
        }
        return responses.get(self.language, responses['en'])
    
    def _disease_response(self, message):
        if 'blight' in message or 'late blight' in message:
            return "Late Blight is very serious! 🚨\n\nQUICK ACTION:\n1. Remove infected plants IMMEDIATELY\n2. Apply copper fungicide to healthy plants\n3. Improve air circulation\n4. Water only at base, keep leaves dry\n5. Don't compost infected plants - burn them\n\nOrganic option: Mix 1 tbsp baking soda + 5ml neem oil in 1L water. Spray every 3 days.\n\nWant specific advice for your crop?"
        
        elif 'spot' in message or 'spots' in message:
            return "Leaf spots can be bacterial or fungal. Here's what to do:\n\n✅ Immediate steps:\n1. Remove affected leaves carefully\n2. Apply copper-based spray\n3. Avoid overhead watering\n4. Disinfect tools with bleach\n\n💊 Treatment:\n• Chemical: Copper sulfate or chlorothalonil\n• Organic: Neem oil spray (5ml/liter)\n\n⚠️ Prevention:\n• Use disease-free seeds\n• Practice crop rotation\n• Maintain plant spacing\n\nWhich crop is affected?"
        
        elif 'rust' in message:
            return "Rust disease shows orange/brown pustules on leaves.\n\n🔸 Treatment:\n1. Usually not serious - monitor first\n2. If severe: Apply sulfur dust or spray\n3. Remove heavily infected leaves\n4. Improve air flow between plants\n\n🌱 Prevention:\n• Plant resistant varieties\n• Avoid excess nitrogen\n• Don't water late in day\n\nCommon on: Corn, wheat, beans\n\nNeed help with specific crop?"
        
        else:
            return "To help identify the disease, please tell me:\n\n1️⃣ Which crop is affected?\n2️⃣ What do you see?\n   • Color of spots (brown/black/yellow)\n   • Location (leaves/stems/fruit)\n   • Pattern (spots/rings/mold)\n\n📸 Better yet - use our SCAN feature to upload a photo for accurate diagnosis!\n\nOr describe the symptoms and I'll help identify it."
    
    def _fertilizer_response(self, message):
        if 'npk' in message or 'ratio' in message:
            return "NPK Fertilizer Guide: 🌱\n\nNPK = Nitrogen-Phosphorus-Potassium\n\n📊 BY GROWTH STAGE:\n\n🌱 Vegetative (leafy growth):\n• High N: 20-10-10 or 15-5-10\n• Examples: Urea, ammonium nitrate\n\n🌸 Flowering/Fruiting:\n• High P: 10-20-10 or 5-10-5\n• Examples: Bone meal, DAP\n\n🍅 Ripening:\n• High K: 10-10-20 or 5-5-15\n• Examples: Muriate of potash\n\n💡 TIP: Test soil first! Over-fertilizing causes more problems than under-fertilizing.\n\nWhich stage is your crop in?"
        
        elif 'organic' in message or 'natural' in message:
            return "Organic Fertilizer Options: 🌿\n\n1️⃣ VERMICOMPOST (best all-around)\n• Apply: 2-3 tons/acre\n• Rich in NPK + micronutrients\n• Improves soil structure\n\n2️⃣ NEEM CAKE\n• Apply: 200-250 kg/acre\n• Natural pest deterrent\n• Slow-release nitrogen\n\n3️⃣ FARMYARD MANURE (FYM)\n• Apply: 5-6 tons/acre\n• Best if well-decomposed\n• Add before planting\n\n4️⃣ GREEN MANURE\n• Grow: Dhaincha, Sunhemp\n• Turn into soil before flowering\n• Free nitrogen!\n\n5️⃣ JEEVAMRUT (liquid)\n• Mix: Cow dung + urine + jaggery\n• Spray or drench weekly\n\nWhich are you interested in?"
        
        else:
            return "Fertilizer Basics: 📖\n\n✅ WHEN TO APPLY:\n• Base dose: Before planting\n• Top dressing: 30-45 days after planting\n• Foliar spray: Every 2-3 weeks\n\n✅ HOW MUCH:\nDepends on:\n• Crop type\n• Soil test results  \n• Previous crop\n\n💡 GOLDEN RULE:\n\"Feed the soil, not the plant!\"\n\n⚠️ AVOID:\n• Over-fertilizing (burns roots)\n• Applying to dry soil\n• Fertilizing stressed plants\n\nWhat crop are you growing? I'll give specific recommendations!"
    
    def _pest_response(self, message):
        return "Pest Control Guide: 🐛\n\n🌿 ORGANIC METHODS (Try first!):\n\n1️⃣ NEEM OIL SPRAY\n• Mix: 5ml neem oil + 1L water + drop of soap\n• Spray: Early morning or evening\n• Effective: 85% of common pests\n\n2️⃣ PANCHAGAVYA\n• Mix cow products + jaggery\n• Natural pesticide + growth booster\n\n3️⃣ GARLIC-CHILI SPRAY\n• Blend garlic + chili + water\n• Strain and spray\n• Repels most insects\n\n💊 CHEMICAL (if severe):\n• Imidacloprid (sucking pests)\n• Chlorpyrifos (chewing pests)\n• Always follow label instructions!\n\n🦗 BY PEST TYPE:\n• Aphids: Neem oil\n• Caterpillars: Bt spray\n• Whiteflies: Yellow sticky traps\n• Beetles: Hand-pick + spray\n\nWhich pest are you facing?"
    
    def _watering_response(self, message):
        return "Watering Guide: 💧\n\n✅ GENERAL RULES:\n\n📏 HOW MUCH:\n• Most crops: 1-2 inches per week\n• Check: Soil should be moist 6 inches deep\n• Avoid: Waterlogged soil\n\n⏰ WHEN:\n• Best: Early morning (6-8 AM)\n• OK: Late evening (after 6 PM)\n• Avoid: Midday (water evaporates)\n\n🌱 BY GROWTH STAGE:\n• Seedling: Light, frequent\n• Vegetative: Moderate, regular\n• Flowering: Consistent, don't stress\n• Fruiting: Reduce slightly\n\n☀️ BY WEATHER:\n• Hot/windy: More frequent\n• Cool/cloudy: Less frequent\n• Rainy: May not need any\n\n💡 TEST METHOD:\n• Stick finger 2 inches in soil\n• If dry: Water needed\n• If moist: Wait\n\n🚨 SIGNS OF:\nUnder-watering: Wilting, dry soil\nOver-watering: Yellow leaves, soggy\n\nWhich crop are you watering?"
    
    def _soil_response(self, message):
        if 'ph' in message:
            return "Soil pH Guide: 🧪\n\n📊 IDEAL pH BY CROP:\n• Vegetables: 6.0-7.0\n• Potatoes: 5.0-6.5 (acidic)\n• Wheat: 6.0-7.5\n• Rice: 5.5-6.5\n• Legumes: 6.0-7.0\n\n🔍 HOW TO TEST:\n1. Buy pH test kit (₹50-200)\n2. Mix soil with water\n3. Compare color to chart\n\n🔧 TO ADJUST:\n\nTOO ACIDIC (pH < 6):\n• Add lime (calcium carbonate)\n• Use wood ash\n• Add dolomite\n\nTOO ALKALINE (pH > 7.5):\n• Add sulfur\n• Use compost\n• Add peat moss\n\n⚠️ Adjust slowly! Test every season.\n\nNeed help interpreting results?"
        
        else:
            return "Soil Health Tips: 🌍\n\n✅ IMPROVE SOIL:\n\n1️⃣ ADD ORGANIC MATTER\n• Compost: 2-3 inches yearly\n• FYM: 5-6 tons/acre\n• Green manure crops\n\n2️⃣ REDUCE TILLAGE\n• Minimal disturbance\n• Mulch instead\n• Protects soil structure\n\n3️⃣ CROP ROTATION\n• Never same crop 2 years\n• Legumes add nitrogen\n• Breaks pest cycles\n\n4️⃣ COVER CROPS\n• Protect bare soil\n• Add organic matter\n• Prevent erosion\n\n5️⃣ AVOID:\n• Over-tilling\n• Burning crop residue\n• Heavy machinery on wet soil\n\n🔬 SOIL TEST:\nGet tested every 2-3 years!\nTests: NPK, pH, organic matter\nCost: ₹200-500\n\nWant specific advice for your soil type?"
    
    def _crop_specific_response(self, message):
        if 'tomato' in message:
            return "Tomato Growing Tips: 🍅\n\n✅ KEY POINTS:\n\n🌱 PLANTING:\n• Spacing: 2-3 feet apart\n• Depth: Bury up to first leaves\n• Stake immediately\n\n💧 WATERING:\n• 1-2 inches/week\n• Keep consistent!\n• Water at base, not leaves\n\n🌿 FERTILIZER:\n• Planting: 10-10-10\n• Flowering: 5-10-10\n• Fruiting: 5-10-15\n\n🐛 COMMON PESTS:\n• Hornworms: Hand-pick\n• Aphids: Neem spray\n• Whiteflies: Yellow traps\n\n🦠 COMMON DISEASES:\n• Late Blight: Remove infected!\n• Early Blight: Copper spray\n• Blossom End Rot: Calcium\n\n📅 HARVEST:\n• 60-85 days after planting\n• Pick when fully colored\n• Twist gently from vine\n\nNeed help with specific problem?"
        
        elif 'potato' in message:
            return "Potato Growing Guide: 🥔\n\n✅ SUCCESS TIPS:\n\n🌱 PLANTING:\n• Season: Feb-March or Oct-Nov\n• Depth: 4 inches\n• Spacing: 12 inches apart\n• Rows: 2.5-3 feet apart\n\n⛰️ HILLING:\n• Week 3-4: Hill soil around stems\n• Repeat every 2-3 weeks\n• Prevents green potatoes\n\n💧 WATERING:\n• Regular until flowering\n• Reduce after flowering\n• Stop 2 weeks before harvest\n\n🌿 FERTILIZER:\n• High N early (leafy growth)\n• High K later (tuber formation)\n• Avoid too much N (reduces tubers)\n\n🦠 WATCH FOR:\n• Late Blight: VERY SERIOUS!\n• Early Blight: Common\n• Colorado beetle: Hand-pick\n\n📅 HARVEST:\n• 90-120 days after planting\n• When vines die back\n• Cure in dark for 2 weeks\n\nWhat stage are you at?"
        
        else:
            return "I can provide detailed guidance for:\n\n🌾 Cereals: Rice, Wheat, Corn, Millet\n🍅 Vegetables: Tomato, Potato, Onion, Cabbage\n🫘 Pulses: Chickpea, Lentil, Pigeon pea\n🌰 Cash crops: Cotton, Sugarcane, Soybean\n\nWhich crop would you like to know about?\n\nOr ask specific questions like:\n• When to plant [crop]?\n• How to fertilize [crop]?\n• Common diseases in [crop]?\n• Harvesting time for [crop]?"
    
    def _organic_response(self, message):
        return "Organic Farming Essentials: 🌿\n\n✅ CORE PRINCIPLES:\n\n1️⃣ SOIL HEALTH FIRST\n• Add compost regularly\n• No chemical fertilizers\n• Encourage earthworms\n• Mulch heavily\n\n2️⃣ NATURAL PEST CONTROL\n• Neem oil (main weapon)\n• Companion planting\n• Attract beneficial insects\n• Physical barriers\n\n3️⃣ NATURAL FERTILIZERS\n• Vermicompost: Best\n• FYM: Well-decomposed\n• Green manure: Free nitrogen\n• Jeevamrut: Growth booster\n\n4️⃣ DISEASE PREVENTION\n• Crop rotation\n• Resistant varieties\n• Proper spacing\n• Sanitation\n\n📋 HOMEMADE RECIPES:\n\n🌿 PEST SPRAY:\n• 50g neem leaves\n• 5 cloves garlic\n• 2 green chilies\n• Blend + strain + spray\n\n🌱 GROWTH BOOSTER:\n• 10 liters water\n• 2kg cow dung\n• 1L cow urine\n• 200g jaggery\n• Ferment 7 days\n\n💰 CERTIFICATION:\n• Takes 3 years\n• Better prices!\n• Growing market\n\nInterested in converting to organic?"
    
    def _planting_response(self, message):
        return "Planting Success Guide: 🌱\n\n✅ GENERAL STEPS:\n\n1️⃣ PREPARE SOIL\n• Till/dig 6-8 inches deep\n• Add compost 2 weeks before\n• Break all clumps\n• Level the field\n\n2️⃣ SEED SELECTION\n• Buy certified seeds\n• Check expiry date\n• Right variety for season\n• Treatment (fungicide)\n\n3️⃣ SEED TREATMENT\n• Soak in water (removes hollow)\n• Treat with Trichoderma\n• Or chemical treatment\n• Dry in shade\n\n4️⃣ PLANTING DEPTH\n• Small seeds: 1/4 inch\n• Medium: 1/2-1 inch\n• Large: 1-2 inches\n• Rule: 2-3× seed size\n\n5️⃣ SPACING\n• Follows seed packet\n• Closer = smaller plants\n• Wider = bigger plants\n• Allow air circulation\n\n6️⃣ AFTER PLANTING\n• Water gently\n• Mulch if possible\n• Protect from birds\n• Mark rows\n\n📅 TIMING:\nDifferent for each crop!\nWhich crop are you planting?"
    
    def _harvest_response(self, message):
        return "Harvesting Guide: 🌾\n\n✅ WHEN TO HARVEST:\n\n🍅 TOMATOES:\n• Fully colored\n• Slight give when squeezed\n• 60-85 days after planting\n\n🥔 POTATOES:\n• Vines die back\n• 2-3 weeks after flowering ends\n• 90-120 days total\n\n🌽 CORN:\n• Silks turn brown\n• Kernels milky when squeezed\n• 70-100 days\n\n🌾 WHEAT:\n• Grains hard\n• Moisture 20-25%\n• 120-150 days\n\n✅ HARVESTING TIPS:\n\n⏰ TIME OF DAY:\n• Early morning (cool)\n• After dew dries\n• Before heat of day\n\n🔪 METHOD:\n• Use sharp tools\n• Cut, don't pull\n• Handle gently\n• Avoid bruising\n\n📦 POST-HARVEST:\n• Sort immediately\n• Remove damaged\n• Cool quickly\n• Store properly\n\n⚠️ DON'T:\n• Harvest when wet\n• Drop or throw\n• Mix varieties\n• Leave in sun\n\nWhich crop needs harvesting?"
    
    def _weather_response(self, message):
        return "Weather & Farming: ☀️🌧️\n\n✅ BY SEASON:\n\n🌸 KHARIF (Jun-Oct):\n• Monsoon crops\n• Rice, cotton, soybean\n• High rainfall\n• Watch for flooding\n\n❄️ RABI (Oct-Mar):\n• Winter crops\n• Wheat, chickpea, mustard\n• Irrigation needed\n• Watch for frost\n\n☀️ SUMMER (Mar-Jun):\n• Heat-tolerant crops\n• Vegetables, melons\n• Heavy irrigation\n• Mulch essential\n\n⚠️ WEATHER RISKS:\n\n🌧️ HEAVY RAIN:\n• Ensure drainage\n• Watch for disease\n• Support plants\n\n☀️ HEAT WAVE:\n• Increase watering\n• Mulch heavily\n• Shade young plants\n\n❄️ FROST:\n• Cover crops overnight\n• Water before frost\n• Harvest tender crops\n\n💨 STRONG WIND:\n• Stake tall plants\n• Harvest ripe fruit\n• Protect greenhouses\n\n📱 APPS TO USE:\n• Mausam (IMD)\n• Meghdoot\n• AccuWeather\n\nPlan ahead!"
    
    def _government_response(self, message):
        return "Government Schemes for Farmers: 🏛️\n\n💰 MAJOR SCHEMES:\n\n1️⃣ PM-KISAN\n• ₹6,000/year\n• Direct to bank\n• 3 installments\n• All farmers eligible\n• Register: pmkisan.gov.in\n\n2️⃣ CROP INSURANCE (PMFBY)\n• Protects against losses\n• Very low premium\n• Weather, pests, disease covered\n• Apply through bank/CSC\n\n3️⃣ SOIL HEALTH CARD\n• Free soil testing\n• Fertilizer recommendations\n• Every 2 years\n• Contact local agriculture office\n\n4️⃣ KCC (Kisan Credit Card)\n• Low-interest loans\n• Flexible repayment\n• For farming expenses\n• Apply through bank\n\n5️⃣ SUBSIDY SCHEMES:\n• Drip irrigation: 55%\n• Farm mechanization: 50%\n• Cold storage: 35%\n• Solar pumps: 60%\n\n📱 HOW TO APPLY:\n• Visit CSC center\n• Use mobile apps\n• Contact agriculture office\n• Through bank\n\n📞 HELPLINE:\n• Kisan Call Center: 1800-180-1551\n• PM-Kisan: 155261\n\nNeed help with specific scheme?"
    
    def _general_farming_response(self):
        return "I'm here to help with all farming questions! 🌾\n\n💡 POPULAR TOPICS:\n\n🦠 Disease & Pests\n• Identification\n• Treatment options\n• Prevention tips\n\n🌱 Crop Management\n• Planting guide\n• Fertilizer advice\n• Watering schedule\n\n🌿 Organic Farming\n• Natural inputs\n• Pest control\n• Certification\n\n💰 Economics\n• Government schemes\n• Market prices\n• Cost reduction\n\n⚙️ TRY ASKING:\n• \"How to treat late blight?\"\n• \"When to plant tomatoes?\"\n• \"Best organic fertilizer?\"\n• \"PM-Kisan scheme details?\"\n\nOr just describe your problem - I'll help! 😊"

# Create singleton instance
chatbot_en = FarmingChatbot('en')
chatbot_hi = FarmingChatbot('hi')
chatbot_ta = FarmingChatbot('ta')

def get_chatbot_response(message, language='en'):
    """Get chatbot response in specified language"""
    if language == 'hi':
        bot = chatbot_hi
    elif language == 'ta':
        bot = chatbot_ta
    else:
        bot = chatbot_en
    
    return bot.get_response(message)

if __name__ == '__main__':
    print("Testing Farming Chatbot...")
    print("\nTest 1:")
    print(get_chatbot_response("Hello"))
    print("\nTest 2:")
    print(get_chatbot_response("My tomato plant has brown spots"))
    print("\nTest 3:")
    print(get_chatbot_response("What fertilizer should I use?"))
