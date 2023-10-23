![](app_ui.png)
In this project, we classify scientists faces, classification restricted to only these 4 scientists:
1. Alan Turing
2. Albert Einstein
3. Issac Newton
4. Marie Curie

## Dataset:
This dataset collected by scraping google for images using chrome extension `Fatkun`.

Data was cleaned by detecing faces and eyes in the image using `OpenCV` Haar Cascade and extract only that region

![](cleaning_snapshot.png)

Then, I did some manul cleaning to remove unwanted, mislabeled or blurry images, the clean data was stored in `dataset/cropped` folder.

## Application:
I built a streamlit web app, the code in `application` folder.

to run the app, navigate to `application` folder and execute these commands:

```
pip install -r requirements.txt
```

```
streamlit run app.py
```