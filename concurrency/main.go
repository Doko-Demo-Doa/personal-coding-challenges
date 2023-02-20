package main

import (
	"fmt"
	"net/http"
	"sync"
)

var wg sync.WaitGroup

func main() {
	websites := []string{
		"https://stackoverflow.com/",
		"https://github.com/",
		"https://www.linkedin.com/",
		"https://medium.com/",
		"https://golang.org/",
		"https://www.udemy.com/",
		"https://www.coursera.org/",
		"https://wesionary.team/",
	}

	for _, website := range websites {
		go getWebsite(website)
		wg.Add(1)
	}

	wg.Wait()
}

func getWebsite(website string) {
	defer wg.Done()
	if res, err := http.Get(website); err != nil {
		println(website + " is down")
	} else {
		fmt.Printf("[%d] %s is up\n", res.StatusCode, website)
	}
}
