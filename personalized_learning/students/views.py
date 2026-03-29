import joblib
import numpy as np
from django.shortcuts import render
from .forms import StudentForm
from .models import Student, Performance, Course

model = joblib.load("best_model.pkl")

def home(request):
    return render(request, 'students/home.html')

def get_risk_level(predicted_G3):
    if predicted_G3 < 10:
        return "High Risk"
    elif predicted_G3 < 13:
        return "Medium Risk"
    else:
        return "Low Risk"

def predict_student(request):
    prediction = None
    risk = None

    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():

            # Get form data
            name = form.cleaned_data['name']
            matric_no = form.cleaned_data['matric_no']
            study_time = form.cleaned_data['study_time']
            absences = form.cleaned_data['absences']
            failures = form.cleaned_data['failures']
            G1 = form.cleaned_data['G1']
            G2 = form.cleaned_data['G2']

            # Prepare ML input
            X = np.array([[G1, G2, study_time, failures, absences]])

            # Predict
            predicted_G3 = model.predict(X)[0]
            prediction = round(predicted_G3, 2)

            # Risk level
            risk = get_risk_level(prediction)

            # Save Student
            student, created = Student.objects.get_or_create(
                matric_no=matric_no,
                defaults={'name': name, 'study_time': study_time, 'absences': absences, 'failures': failures}
            )

            # Save Performance
            Performance.objects.create(
                student=student,
                G1=G1,
                G2=G2,
                predicted_G3=prediction,
                risk_level=risk
            )

    else:
        form = StudentForm()

    return render(request, 'students/predict.html',
                  {'form': form, 'prediction': prediction, 'risk': risk})