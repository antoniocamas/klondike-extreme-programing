MY_PATH="`dirname \"$0\"`"              # relative
MY_PATH="`( cd \"$MY_PATH\" && pwd )`"  # absolutized and normalized
if [ -z "$MY_PATH" ] ; then
  exit 1 
fi

pushd "$MY_PATH/.." > /dev/null
   nosetests-3.4 -s test/
popd > /dev/null


