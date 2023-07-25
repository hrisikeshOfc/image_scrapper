## Simplified Deployment of Image Scraper Project using chromedriver-binary and Flask

## Introduction

In this document, we will discuss the reasons behind using the `chromedriver-binary` package instead of `chromedriver.exe` and the decision to create a Flask application (`app.py`) for deploying the image scraper project. We will explore the benefits and advantages of these choices, especially when deploying the application using Docker.

### Part 1: Using `chromedriver-binary` Package

#### Background

The image scraper project requires the use of a web browser automation tool to interact with websites and extract images. Traditionally, developers would manually install and manage the `chromedriver.exe` executable for Chrome browser automation in their local environments. However, when it comes to deploying the project, managing dependencies like `chromedriver.exe` becomes cumbersome, especially when using containerization with Docker.

#### Rationale

To alleviate the complexities associated with managing `chromedriver.exe`, we made a strategic decision to use the `chromedriver-binary` package in our Python project. The `chromedriver-binary` package is a Python library that provides a convenient and streamlined approach to handle the ChromeDriver executable. Instead of manually managing the executable file, this package automatically downloads the appropriate ChromeDriver version compatible with the installed Chrome browser.

#### Benefits of `chromedriver-binary`

1. **Simplified Deployment:** The `chromedriver-binary` package ensures seamless deployment by automatically handling the appropriate ChromeDriver version, eliminating the need for manual setup and dependency management.

2. **Cross-platform Compatibility:** Using `chromedriver-binary` enhances the cross-platform compatibility of the image scraper project. Developers can now deploy the application on various operating systems without worrying about platform-specific executable files.

3. **Easy Updates:** As Chrome browser versions are periodically updated, the `chromedriver-binary` package ensures that the corresponding ChromeDriver version is automatically installed, enabling the project to stay up-to-date with the latest browser features and bug fixes.

4. **Dockerization:** The `chromedriver-binary` package is especially well-suited for Dockerized deployments, where automated dependency management is crucial for creating lightweight and consistent containers.

### Part 2: Creating a Flask Application for Deployment

#### Background

Initially, the image scraper project was organized as a collection of Python modules, with the main functionality residing in a module called `scrapper.py`. While this setup worked well during development, it posed challenges when deploying the project as a standalone application.

#### Rationale

To simplify deployment and provide an easy-to-use interface for the image scraper project, we opted to create a Flask application (`app.py`). Flask is a lightweight and powerful web framework that allows us to expose the image scraping functionality through HTTP endpoints.

#### Benefits of Using Flask

1. **API-Based Approach:** With Flask, we can structure the image scraper project as an API, providing clear and well-defined endpoints for interacting with the scraper functionality. This allows other applications to easily integrate and utilize the scraper.

2. **Web Interface (Optional):** By creating a Flask application, we have the option to build a user-friendly web interface for the image scraper project. Users can interact with the scraper through a browser, making it more accessible and user-friendly.

3. **Asynchronous Support:** Flask enables us to implement asynchronous behavior, which can be particularly useful when handling multiple scraping requests simultaneously, enhancing the overall performance and responsiveness of the application.

4. **Integration with Docker:** Flask applications are well-suited for containerization using Docker. We can efficiently package the image scraper project as a Docker container and deploy it on various platforms and cloud services.

5. **Scalability:** Flask applications can be deployed on various web servers and cloud platforms, allowing easy scalability to accommodate increased traffic and user demand.

### Conclusion

In conclusion, by using the `chromedriver-binary` package and creating a Flask application for deployment, we have significantly simplified the process of deploying and managing the image scraper project. The combination of automated dependency handling and a user-friendly API makes it easier for other developers to use and integrate the scraper into their own applications. Moreover, the flexibility of Dockerization and Flask's lightweight nature further supports seamless deployment across various environments and cloud platforms.

## Deployment steps
There's a seperate document we have created for the deployment steps thoroughly for this project. 

Go check it out [here]("https://github.com/hrisikeshOfc/image_scrapper/blob/5b5f03d29a0fe58d3a2d21f9684e0c661c3b2a78/documents/render_deployment.pdf)