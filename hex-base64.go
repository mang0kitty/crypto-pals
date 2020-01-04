package main

import 
(
	"encoding/hex"
	"encoding/base64"
	"fmt"
	"log"
)

func main(){
	hex_string := "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"

decoded_hex, err := hex.DecodeString(hex_string)
if err != nil{
	log.Fatalf("hex.DecodeString() failed with '%s'\n", err.Error())
}
fmt.Printf("hex: %s\n", decoded_hex)

encoded_base64 := base64.StdEncoding.EncodeToString(decoded_hex)
fmt.Printf("base64: %s\n", encoded_base64)
}
	

