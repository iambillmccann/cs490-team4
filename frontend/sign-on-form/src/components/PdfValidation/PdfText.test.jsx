import { isPDF, inputCharLength } from "./PdfTextValidation.jsx";


//Test suite
describe("Valid file extension(PDF) and file size", () => {
  //test case 1: is pdf ?
  it("should return true for valid PDF file", () => {

  });

   //test case 2: is not pdf ?
   it("should return false for invalid file extension", () => {

   });


  //test case 3: is pdf file less or equal to 2MB
  it("should return true for file size <= 2MB", () => {

  });

  //test case 3: is pdf file greater than 2MB
  it("should return false for file size > 2MB", () => {

  });
})


//Test suite 2
describe("valid input length", () => {

  //test case 1: input is <= 5000 characters
  it("should return true for text input with <= 5000 characters", () => {

  });

  //test case 2: input is <= 5000 characters
  it("should return false for text input with > 5000 characters", () => {
    
  });

})