async function main() {
    const CourseNFT = await ethers.getContractFactory("courseNFT")
  
    // Start deployment, returning a promise that resolves to a contract object
    const courseNFT = await CourseNFT.deploy()
    await courseNFT.deployed()
    console.log("Contract deployed to address:", courseNFT.address)
  }
  
  main()
    .then(() => process.exit(0))
    .catch((error) => {
      console.error(error)
      process.exit(1)
    })
  