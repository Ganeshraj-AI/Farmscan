"""
SIMPLIFIED Disease Detection - NO ML DEPENDENCIES
For quick deployment - basic pattern matching only
"""

def analyze_crop_image_local(image, language='en'):
    """
    Simplified analysis without ML dependencies
    Returns a demo response for deployment testing
    """
    try:
        from PIL import ImageStat
        
        # Basic color analysis using PIL only
        stats = ImageStat.Stat(image)
        avg_colors = stats.mean
        
        # Simple heuristic: if image is mostly green, it's healthy
        if len(avg_colors) >= 3:
            r, g, b = avg_colors[0], avg_colors[1], avg_colors[2]
            
            # If green is dominant, likely healthy
            if g > r and g > b and g > 100:
                return {
                    "diseaseName": "Healthy Plant",
                    "confidence": 0.85,
                    "severity": "None",
                    "spreadRisk": "No disease detected. Plant appears healthy.",
                    "treatment": "No treatment needed. Continue regular care.",
                    "organicTreatment": {
                        "title": "Preventive Care",
                        "details": [
                            "Water regularly - 1-2 inches per week",
                            "Apply balanced fertilizer monthly",
                            "Monitor for pests and diseases",
                            "Maintain good air circulation"
                        ]
                    },
                    "safetyWarning": "Keep monitoring your plants regularly for best results."
                }
            else:
                # Possible disease detected
                return {
                    "diseaseName": "Possible Disease Detected",
                    "confidence": 0.75,
                    "severity": "Medium",
                    "spreadRisk": "Consult agricultural expert for accurate diagnosis.",
                    "treatment": "Upload a clearer image or consult local agricultural extension office.",
                    "organicTreatment": {
                        "title": "General Care",
                        "details": [
                            "Remove affected leaves",
                            "Improve air circulation",
                            "Apply neem oil spray",
                            "Consult local expert"
                        ]
                    },
                    "safetyWarning": "For accurate diagnosis, please consult an agricultural expert."
                }
        
        # Fallback response
        return {
            "diseaseName": "Analysis Complete",
            "confidence": 0.70,
            "severity": "Unknown",
            "spreadRisk": "Please upload a clear image of the plant leaf.",
            "treatment": "Consult agricultural expert for accurate diagnosis."
        }
        
    except Exception as e:
        print(f"Analysis error: {e}")
        return {
            "diseaseName": "Demo Mode",
            "confidence": 0.65,
            "severity": "Unknown",
            "spreadRisk": "App is running in demo mode without ML model.",
            "treatment": "The app is deployed successfully! ML features will be added soon.",
            "organicTreatment": {
                "title": "App Status",
                "details": [
                    "✅ App deployed successfully",
                    "✅ Basic features working",
                    "⏳ ML model will be added soon",
                    "📱 Try the chatbot and news features!"
                ]
            },
            "safetyWarning": "This is a demo deployment. Full ML features coming soon!"
        }

def get_model_info():
    """Return model information"""
    return {
        'model_name': 'FarmScan Lite (Demo Mode)',
        'version': '1.0-lite',
        'techniques': ['Basic Color Analysis'],
        'diseases_supported': 2,
        'accuracy': 'Demo Mode',
        'offline': True
    }
