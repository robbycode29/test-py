FROM python:3.7-alpine

COPY . .

CMD ["python", "manageStudents.py"]

EXPOSE 8080