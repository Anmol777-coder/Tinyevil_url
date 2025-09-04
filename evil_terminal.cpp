#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <ctime>
#include <csignal>
#include <unistd.h>
#include <netdb.h>
#include <arpa/inet.h>
#include <curl/curl.h>

using namespace std;

#define GREEN  "\033[92m"
#define BLUE   "\033[94m"
#define CYAN   "\033[96m"
#define RED    "\033[91m"
#define YELLOW "\033[93m"
#define RESET  "\033[0m"

bool running = true;

size_t WriteCallback(void* contents, size_t size, size_t nmemb, void* userp) {
    ((string*)userp)->append((char*)contents, size * nmemb);
    return size * nmemb;
}

void banner() {
    system("clear");
    cout << GREEN << "             .           .           \n";
    cout << "             M.          .M          \n";
    cout << "              MMMMMMMMMMM.           \n";
    cout << "           .MMM\\\\MMMMMMM/MMM.         \n";
    cout << "          .MMM.7MMMMMMM.7MMM.        \n";
    cout << "         .MMMMMMMMMMMMMMMMMMM        \n";
    cout << "         MMMMMMM.......MMMMMMM       \n";
    cout << "         MMMMMMMMMMMMMMMMMMMMM       \n";
    cout << "    MMMM MMMMMMMMMMMMMMMMMMMMM MMMM  \n";
    cout << "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \n";
    cout << "   dMMMM.MMMMMMMMMMMMMMMMMMMMM.MMMMD \n";
    cout << "    MMM8 MMMMMMMMMMMMMMMMMMMMM 8MMM  \n";
    cout << "         MMMMMMMMMMMMMMMMMMMMM       \n";
    cout << "             MMMMM   MMMMM  v3.0     \n";
    cout << "             .MMM.   .MMM.           \n";
    cout << CYAN  << "          TinyURL GPT - Evil Terminal\n";
    cout << CYAN  << "============================================================\n" << RESET;
}

string shortenURL(const string& longUrl) {
    CURL* curl;
    CURLcode res;
    string readBuffer;
    string requestUrl = "http://tinyurl.com/api-create.php?url=" + longUrl;

    curl = curl_easy_init();
    if (curl) {
        curl_easy_setopt(curl, CURLOPT_URL, requestUrl.c_str());
        curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
        curl_easy_setopt(curl, CURLOPT_WRITEDATA, &readBuffer);
        res = curl_easy_perform(curl);
        curl_easy_cleanup(curl);
    }
    return readBuffer.empty() ? "[!] Failed to shorten link" : readBuffer;
}

string generateSessionID(int length = 12) {
    string chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789";
    string result;
    srand(time(0));
    for (int i = 0; i < length; i++) {
        result += chars[rand() % chars.size()];
    }
    return result;
}

void saveHistory(const string& original, const string& shortUrl) {
    ofstream file("link_history.txt", ios::app);
    if (file.is_open()) {
        time_t now = time(0);
        file << "[" << ctime(&now) << "] " << original << " -> " << shortUrl << "\n";
        file.close();
    }

    ofstream html("link_history.html", ios::app);
    if (html.tellp() == 0) {
        html << "<html><head><title>Link History</title></head><body><table border=1>";
        html << "<tr><th>Date & Time</th><th>Original</th><th>Shortened</th></tr>";
    }
    time_t now = time(0);
    html << "<tr><td>" << ctime(&now) << "</td><td>" << original << "</td><td><a href='" << shortUrl << "'>" << shortUrl << "</a></td></tr>";
    html.close();
}

void showHistory() {
    ifstream file("link_history.txt");
    if (!file.is_open()) {
        cout << RED << "[!] No history found.\n" << RESET;
        return;
    }
    string line;
    cout << CYAN << "\n=== Link History ===\n" << RESET;
    while (getline(file, line)) {
        cout << line << endl;
    }
    file.close();
}

void checkInternet() {
    cout << BLUE << "[*] Checking Internet Connection..." << RESET << endl;
    int res = system("ping -c 1 google.com > /dev/null 2>&1");
    if (res == 0) {
        cout << GREEN << "[+] Internet: CONNECTED ✅\n" << RESET;
        char hostname[256];
        gethostname(hostname, sizeof(hostname));
        struct hostent* h = gethostbyname(hostname);
        if (h) {
            cout << YELLOW << "[i] Local IP: " << GREEN << inet_ntoa(*((struct in_addr*)h->h_addr)) << RESET << endl;
        }
        CURL* curl = curl_easy_init();
        string publicIP;
        if (curl) {
            curl_easy_setopt(curl, CURLOPT_URL, "https://api.ipify.org");
            curl_easy_setopt(curl, CURLOPT_WRITEFUNCTION, WriteCallback);
            curl_easy_setopt(curl, CURLOPT_WRITEDATA, &publicIP);
            curl_easy_perform(curl);
            curl_easy_cleanup(curl);
        }
        cout << YELLOW << "[i] Public IP: " << GREEN << (publicIP.empty() ? "Unavailable" : publicIP) << RESET << endl;
    } else {
        cout << RED << "[!] Internet: FAILED ❌\n" << RESET;
        exit(1);
    }
}

void ctrlCHandler(int sig) {
    cout << RED << "\n[*] (Ctrl + C) Detected, Exiting...\n" << RESET;
    running = false;
    exit(0);
}

int main() {
    signal(SIGINT, ctrlCHandler);
    banner();
    checkInternet();

    int choice;
    string url, shortUrl;

    while (running) {
        cout << YELLOW << "\n[1] Shorten a URL\n";
        cout << "[2] View history\n";
        cout << "[3] Generate random session ID\n";
        cout << "[4] Exit\n" << RESET;
        cout << CYAN << "[+] Choose option: " << RESET;
        cin >> choice;

        if (choice == 1) {
            cout << BLUE << "[+] Enter URL: " << RESET;
            cin >> url;
            shortUrl = shortenURL(url);
            cout << GREEN << "[🔗] Shortened URL: " << shortUrl << RESET << endl;
            saveHistory(url, shortUrl);
        } else if (choice == 2) {
            showHistory();
        } else if (choice == 3) {
            cout << GREEN << "[i] Session ID: " << generateSessionID() << RESET << endl;
        } else if (choice == 4) {
            cout << YELLOW << "👋 Goodbye, MONU! Stay safe.\n" << RESET;
            break;
        } else {
            cout << RED << "❌ Invalid option.\n" << RESET;
        }
    }
    return 0;
}
