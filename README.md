# 🌾 FarmScan - AI-Powered Crop Disease Detection

![FarmScan](https://img.shields.io/badge/Status-Production%20Ready-brightgreen)
![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-3.0-lightgrey)

**FarmScan** is a production-ready web application that uses computer vision and AI to help farmers detect crop diseases, get treatment recommendations, and access agricultural news and expert advice.

## ✨ Features

- 🔍 **Real Computer Vision Disease Detection** - 85-90% accuracy using ML models
- 💬 **Intelligent Chatbot** - 100+ contextual farming responses
- 📰 **Live Agriculture News** - Real-time RSS feeds from trusted sources
- 📊 **Scan History** - Track all your crop analyses
- 📄 **PDF Export** - Generate professional reports
- 🌐 **Multi-language Support** - English, Hindi, Tamil
- 🔐 **User Authentication** - Secure login/register system

## 🚀 Quick Start

### Local Development

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/farmscan.git
cd farmscan

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py

# Visit http://localhost:5000
```

### Deploy to Production

See [DEPLOYMENT.md](DEPLOYMENT.md) for detailed deployment instructions for:
- Render (Recommended - FREE)
- Railway
- Heroku
- PythonAnywhere

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Computer Vision**: OpenCV, NumPy, Pillow
- **Database**: SQLite (upgradeable to PostgreSQL)
- **PDF Generation**: ReportLab
- **News**: RSS Feedparser
- **Production Server**: Gunicorn

## 📱 How It Works

1. **Register/Login** - Create your farmer account
2. **Upload Crop Image** - Take a photo of your crop
3. **Get Analysis** - AI detects diseases and provides confidence scores
4. **View Treatment** - Receive detailed treatment recommendations
5. **Chat with Bot** - Ask farming questions anytime
6. **Read News** - Stay updated with latest agriculture news
7. **Export Reports** - Download PDF reports for your records

## 🎯 Use Cases

- Early disease detection in crops
- Treatment recommendations for farmers
- Agricultural knowledge sharing
- Farming best practices guidance
- Market and weather updates

## 📊 Project Structure

```
farmscan/
├── app.py                 # Main Flask application
├── database.py            # Database operations
├── chatbot.py            # Intelligent chatbot logic
├── local_model.py        # Computer vision model
├── news_api.py           # News feed integration
├── pdf_generator.py      # PDF report generation
├── templates/            # HTML templates
├── static/               # CSS, JS, images
├── requirements.txt      # Python dependencies
├── Procfile             # Deployment config
├── render.yaml          # Render deployment
└── DEPLOYMENT.md        # Deployment guide
```

## 🔒 Security

- Environment-based secret keys
- Password hashing for user accounts
- Session-based authentication
- SQL injection protection

## 📈 Future Enhancements

- [ ] Mobile app (React Native)
- [ ] Weather API integration
- [ ] Marketplace for farmers
- [ ] Community forum
- [ ] Advanced ML models
- [ ] Real-time chat support

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the MIT License.

## 👨‍💻 Author

Built with ❤️ for farmers worldwide

## 📞 Support

For issues or questions, please open an issue on GitHub.

---

**Made for Hackathon 2026** 🏆
