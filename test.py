from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

def test_uv_setup():
    """Test UV setup with Grok API"""
    
    print("🧪 Testing UV + LangChain Setup...")
    print("-" * 50)
    
    # Load environment variables
    load_dotenv()
    print("✅ Environment variables loaded")
    
    # Check API key
    api_key = os.getenv("GROK_API_KEY")
    if not api_key:
        print("❌ GROK_API_KEY not found in .env!")
        return False
    print("✅ API key found")
    
    # Create LLM instance
    try:
        llm = ChatGroq(
            model="openai/gpt-oss-120b",
            api_key=api_key,
            temperature=0.5
        )
        print("✅ Grok LLM instance created")
    except Exception as e:
        print(f"❌ Error creating LLM: {e}")
        return False
    
    # Test API call
    try:
        print("\n📞 Making test API call...")
        response = llm.invoke("Say 'UV setup successful!'")
        print(f"✅ API Response: {response.content}")
        print("\n🎉 Everything works perfectly!")
        return True
    except Exception as e:
        print(f"❌ API call failed: {e}")
        return False

if __name__ == "__main__":
    test_uv_setup()