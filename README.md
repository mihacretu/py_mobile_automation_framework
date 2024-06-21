**Create a Virtual Environment**

    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

**Install dependencies**

    pip install -r requirements.txt

**Run tests**

    pytest

 - Make sure appium is up and running.
 - Modify the **PLATFORM** configuration based on the platform for which the tests need to run: **iOS** or **Android**. Default is set to 'Android' if PLATFORM is not set.