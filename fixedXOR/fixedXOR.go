package main

import (
	"encoding/hex"
	"fmt"
	"log"
)

func xor(decodedByteArray, xorInput []byte) []byte {
	xorOutput := make([]byte, len(xorInput))
	for i := 0; i < len(xorInput); i++ {
		xorOutput[i] = decodedByteArray[i] ^ xorInput[i]
	}
	return xorOutput

}

func hexToByteArray(input string) []byte {
	decodedHex, err := hex.DecodeString(input)
	if err != nil {
		log.Fatalf("hex.DecodeString() failed with '%s'\n", err.Error())
	}

	return decodedHex
}

func byteArrayToHex(input []byte) string {
	return hex.EncodeToString(input)
}

func main() {
	hexString := hexToByteArray("1c0111001f010100061a024b53535009181c")
	xorInput := hexToByteArray("686974207468652062756c6c277320657965")

	xorResult := byteArrayToHex(xor(hexString, xorInput))
	fmt.Printf("xor result: '%s'\n", xorResult)
}
