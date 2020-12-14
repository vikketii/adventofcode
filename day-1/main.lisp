(defun main ()
  (let
      ((entries (read-input-as-list input #'parse-integer)))
    print entries))
