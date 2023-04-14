version 1.0

workflow hello_import {
  input {
    String name = "World"
  }
  
  call import_hello {
      input:
          name = name
  }
}

task import_hello {
    input {
      String name
    }
    
    command {
        echo "Hello ${name}!"
    }

    runtime {
        docker: "debian:stable-slim"
    }
    
    output {
        File response = stdout()
    }
}